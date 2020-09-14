package com.skincancerdetection.bffnode.router;

import com.skincancerdetection.bffnode.model.CommonResponse;
import com.skincancerdetection.bffnode.model.UserDetailsDto;

public interface CommonServiceRouter {
    CommonResponse registerUser(UserDetailsDto userDetailsDto);
}
