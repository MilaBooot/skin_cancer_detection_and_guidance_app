package com.skincancerdetection.bffnode.assemble;

import com.skincancerdetection.bffnode.model.*;
import com.skincancerdetection.bffnode.utils.AESEncryptionDecryption;
import com.skincancerdetection.bffnode.utils.SurveyUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.stream.Collectors;

@Component
public class RequestAssembler {

    @Autowired
    private AESEncryptionDecryption encryptionDecryption;

    public UserInfoRequestDto assembleUserInfoRequestDto(AuthenticationRequest request) {
        UserInfoRequestDto userInfoRequestDto = new UserInfoRequestDto();
        userInfoRequestDto.setUser_id(request.getUsername());
        return userInfoRequestDto;
    }

    public UserDetailsDto assembleUserDetailsDto(RegistrationRequest request) {
        UserDetailsDto userDetailsDto = new UserDetailsDto();
        userDetailsDto.setDob(request.getDob());
        userDetailsDto.setFirst_name(request.getFirstname());
        userDetailsDto.setLast_name(request.getLastname());
        final String encypted = encryptionDecryption.encrypt(request.getPassword());
        userDetailsDto.setPassword(encypted);
        userDetailsDto.setUser_id(request.getUsername());
        userDetailsDto.setGender(request.getGender());
        return userDetailsDto;
    }

    public AuthenticationResponse assembleAuthenticationResponse(UserInfoResponseDto userInfoResponseDto
            , String username) {
        AuthenticationResponse response = new AuthenticationResponse();
        response.setFirstname(userInfoResponseDto.getFirst_name());
        response.setLastname(userInfoResponseDto.getLast_name());
        response.setUsername(username);
        return response;
    }

    public ImageProcRequest assembleImageProcRequest(byte[] bytes, String username) {
        ImageProcRequest imageProcRequest = new ImageProcRequest();
        imageProcRequest.setImage(bytes);
        List<SurveyResponseDto> surveyResponseDtoList = SurveyUtil.getResponse(username).getQuestions()
                .stream()
                .map(s -> new SurveyResponseDto(s.getId(), s.getAnswer()))
                .collect(Collectors.toList());
        imageProcRequest.setQuestions(surveyResponseDtoList);
        return imageProcRequest;
    }

    public FileUploadDto assembleFileUploadDto(String username, String desc, MultipartFile file) throws IOException {
        FileUploadDto fileUploadDto = new FileUploadDto();
        fileUploadDto.setDescription(desc);
        fileUploadDto.setUserId(username);
        String filename = file.getOriginalFilename();
        String[] filenameSplit = filename.split("\\.");
        String time = LocalDateTime.now().toString()
                .replaceAll("\\.", "-")
                .replaceAll(":", "-");
        String newFileName = new StringBuilder(filenameSplit[0])
                .append("-")
                .append(time)
                .append(".")
                .append(filenameSplit[1]).toString();
        fileUploadDto.setFilename(newFileName);
        fileUploadDto.setFileByteString(file.getBytes());
        return fileUploadDto;
    }
}
