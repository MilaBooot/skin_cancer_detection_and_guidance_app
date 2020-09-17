package com.skincancerdetection.bffnode.service;

import com.skincancerdetection.bffnode.model.QuestionDto;
import com.skincancerdetection.bffnode.model.UserDetailsDto;
import com.skincancerdetection.bffnode.model.UserInfoRequestDto;
import com.skincancerdetection.bffnode.model.UserInfoResponseDto;

import java.util.List;

public interface CommonService {
    void registerUser(UserDetailsDto userDetailsDto);
    UserInfoResponseDto retrieveUser(UserInfoRequestDto userInfoRequestDto);
    List<QuestionDto> getQuestionnaire();

}
