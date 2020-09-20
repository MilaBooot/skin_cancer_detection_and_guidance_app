package com.skincancerdetection.bffnode.service;

import com.skincancerdetection.bffnode.model.*;

import java.util.List;

public interface CommonService {
    void registerUser(UserDetailsDto userDetailsDto);
    UserInfoResponseDto retrieveUser(UserInfoRequestDto userInfoRequestDto);
    List<QuestionDto> getQuestionnaire();
    public ImageProcReponse getPrediction(ImageProcRequest imageProcRequest);

}
