package com.skincancerdetection.bffnode.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.skincancerdetection.bffnode.model.*;
import com.skincancerdetection.bffnode.router.CommonServiceRouter;
import com.skincancerdetection.bffnode.router.MlServiceRouter;
import com.skincancerdetection.bffnode.utils.AESEncryptionDecryption;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Arrays;
import java.util.List;

@Service
public class CommonServiceImpl implements CommonService{

    @Autowired
    private CommonServiceRouter commonServiceRouter;

    @Autowired
    private MlServiceRouter mlServiceRouter;

    @Autowired
    private ObjectMapper mapper;

    @Override
    public void registerUser(UserDetailsDto userDetailsDto) {
        commonServiceRouter.registerUser(userDetailsDto);
    }

    @Autowired
    private AESEncryptionDecryption encryptionDecryption;

    @Override
    public UserInfoResponseDto retrieveUser(UserInfoRequestDto userInfoRequestDto) {
        CommonResponseData<UserInfoResponseDto> responseData = new CommonResponseData<>();
        CommonResponse<CommonResponseData> response = commonServiceRouter.retrieveUser(userInfoRequestDto);
        responseData = (CommonResponseData<UserInfoResponseDto>)mapper
                .convertValue(response.getResult(), CommonResponseData.class);
        UserInfoResponseDto userInfoResponseDto = mapper
                .convertValue(responseData.getData(), UserInfoResponseDto.class);
        final String decrypted = encryptionDecryption.decrypt(userInfoResponseDto.getPassword());
        userInfoResponseDto.setPassword(decrypted);
        return userInfoResponseDto;

    }

    @Override
    public List<QuestionDto> getQuestionnaire() {
        CommonArrResponseData<QuestionDto[]> responseData = new CommonArrResponseData<>();
        CommonResponse<CommonArrResponseData> response = commonServiceRouter.getQuestionnaire();
        responseData = mapper.convertValue(response.getResult(), CommonArrResponseData.class);
        return Arrays.asList(mapper.convertValue(responseData.getData(), QuestionDto[].class));

    }

    public ImageProcReponse getPrediction(ImageProcRequest imageProcRequest) {
        CommonResponseData<ImageProcReponse> responseData = new CommonResponseData<>();
        CommonResponse<CommonResponseData> response = mlServiceRouter.processImage(imageProcRequest);
        responseData = (CommonResponseData<ImageProcReponse>)mapper
                .convertValue(response.getResult(), CommonResponseData.class);
        return mapper.convertValue(responseData.getData(), ImageProcReponse.class);

    }

}
