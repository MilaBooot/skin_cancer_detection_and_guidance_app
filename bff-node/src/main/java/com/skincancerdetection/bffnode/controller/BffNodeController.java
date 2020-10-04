package com.skincancerdetection.bffnode.controller;

import com.skincancerdetection.bffnode.assemble.RequestAssembler;
import com.skincancerdetection.bffnode.enums.ErrorEnum;
import com.skincancerdetection.bffnode.exception.BffNodeException;
import com.skincancerdetection.bffnode.model.*;
import com.skincancerdetection.bffnode.service.CommonService;
import com.skincancerdetection.bffnode.utils.SurveyUtil;
import org.dozer.DozerBeanMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;

@RestController
public class BffNodeController {

    @Autowired
    private CommonService commonService;

    @Autowired
    private DozerBeanMapper mapper;

    @Autowired
    private RequestAssembler requestAssembler;

    @PostMapping(value="/register")
    public ResponseEntity registerUser(@RequestBody RegistrationRequest request) {

        UserDetailsDto userDetailsDto = requestAssembler.assembleUserDetailsDto(request);
        commonService.registerUser(userDetailsDto);
        return new ResponseEntity(HttpStatus.CREATED);
    }

    @PostMapping(value="/authenticate")
    public ResponseEntity authenticateUser(@RequestBody AuthenticationRequest request) {
        UserInfoRequestDto userInfoRequestDto = requestAssembler.assembleUserInfoRequestDto(request);
        UserInfoResponseDto userInfoResponseDto = commonService.retrieveUser(userInfoRequestDto);

        AuthenticationResponse response = requestAssembler
                .assembleAuthenticationResponse(userInfoResponseDto, request.getUsername());

        if (userInfoResponseDto.getPassword().equalsIgnoreCase(request.getPassword())) {
            return new ResponseEntity(response, HttpStatus.OK);
        } else {
            ErrorMessageDto messageDto = new ErrorMessageDto(ErrorEnum.USER_NOT_FOUND.getErrMessage());
            CommonResponse<ErrorMessageDto> errResponse = new CommonResponse(messageDto);
            return new ResponseEntity(ErrorEnum.USER_NOT_FOUND.getErrMessage(), HttpStatus.NOT_FOUND);
        }


    }

    @GetMapping("/questionnaire")
    public ResponseEntity getQuestionnaire() {
        List<QuestionDto> questionnaireRespons = commonService.getQuestionnaire();
        QuestionnaireResponse response = new QuestionnaireResponse();
        response.setQuestions(questionnaireRespons);
        return new ResponseEntity(response, HttpStatus.OK);

    }

    @PostMapping("/image/{userid}/upload")
    public ResponseEntity upload(@RequestParam("image") MultipartFile multipartFile
            , @PathVariable("userid") String userid) throws IOException {
        byte[] imageByteArr = multipartFile.getBytes();
        if (SurveyUtil.getResponse(userid) == null) {
            ErrorMessageDto messageDto = new ErrorMessageDto(ErrorEnum.UNANSWERED_ERROR.getErrMessage());
            CommonResponse<ErrorMessageDto> errResponse = new CommonResponse(messageDto);
            return new ResponseEntity(ErrorEnum.UNANSWERED_ERROR.getErrMessage(), HttpStatus.BAD_REQUEST);

        }
        ImageProcRequest imageProcRequest = requestAssembler.assembleImageProcRequest(imageByteArr, userid);
        ImageProcReponse reponse = commonService.getPrediction(imageProcRequest);

        return new ResponseEntity(reponse, HttpStatus.OK);
    }

    @PostMapping("/questionnaire-reponse/{userid}/upload")
    public ResponseEntity upload(@RequestBody QuestionnaireResponse questionnaireResponse
            , @PathVariable("userid") String userid) {
        if(questionnaireResponse.getQuestions().isEmpty() && questionnaireResponse.getQuestions().size() ==0) {
            ErrorMessageDto messageDto = new ErrorMessageDto(ErrorEnum.UNANSWERED_ERROR.getErrMessage());
            CommonResponse<ErrorMessageDto> errResponse = new CommonResponse(messageDto);
            return new ResponseEntity(ErrorEnum.UNANSWERED_ERROR.getErrMessage(), HttpStatus.BAD_REQUEST);

        }
        SurveyUtil.recordResponse(questionnaireResponse,userid);
        return new ResponseEntity(HttpStatus.OK);
    }

    @GetMapping("/doctors/{longitude}/{latitude}")
    public ResponseEntity getDoctors(@PathVariable("longitude") double longitude
            , @PathVariable("latitude") double latitude) {
        DoctorEnquiryReponse reponse = new DoctorEnquiryReponse();
        reponse.setDoctors(commonService.getDoctors(longitude, latitude));
        return new ResponseEntity(reponse, HttpStatus.OK);
    }


    @PostMapping("/uploadDocument" )
    public ResponseEntity uploadPrescription(@RequestParam(value = "description") String description,
                                             @RequestParam(value = "file") MultipartFile multipartFile,
                                             @RequestParam(value = "username") String username) throws IOException {
        FileUploadDto fileUploadDto = requestAssembler.assembleFileUploadDto(username, description, multipartFile);
        commonService.uploadDocument(fileUploadDto);
        return new ResponseEntity(HttpStatus.OK);
    }

    @GetMapping("/{userid}/getDocuments")
    public ResponseEntity getUserDocuments(@PathVariable("userid") String userid) {

        List<UserDocuments> reponse = commonService.getUserDocuments(userid);
        return new ResponseEntity(reponse, HttpStatus.OK);
    }

    @GetMapping(value = "/{userid}/getDocument",  produces = MediaType.IMAGE_JPEG_VALUE)
    public ResponseEntity getUserDocumentForDownload(@RequestParam(value = "docFile") String fileName
            , @PathVariable("userid") String userid) throws IOException {
        byte[] fileByteArr = commonService.getFile(userid, fileName);
        return new ResponseEntity(fileByteArr, HttpStatus.OK);
    }

    @DeleteMapping("/{userid}/document")
    public ResponseEntity deleteDocument(@RequestParam(value = "docFile") String fileName
            , @PathVariable("userid") String userid)  {
        commonService.deleteDocument(userid, fileName);
        return new ResponseEntity(HttpStatus.OK);
    }

    @GetMapping("/cancerDetail/{type}")
    public ResponseEntity getCancerDetails(@PathVariable("type") String cancerType) {

        CancerTypeReponse cancerTypeReponse = commonService.getCancerDetails(cancerType);
        return new ResponseEntity(cancerTypeReponse, HttpStatus.OK);
    }

}
