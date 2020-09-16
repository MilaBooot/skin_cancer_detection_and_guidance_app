package com.skincancerdetection.bffnode.router;

import com.skincancerdetection.bffnode.model.CommonResponse;
import com.skincancerdetection.bffnode.model.UserDetailsDto;
import com.skincancerdetection.bffnode.model.UserInfoRequestDto;

public interface CommonServiceRouter {
    CommonResponse registerUser(UserDetailsDto userDetailsDto);
    CommonResponse retrieveUser(UserInfoRequestDto userInfoRequestDto);
}
