package com.skincancerdetection.bffnode.router;

import com.skincancerdetection.bffnode.model.CommonResponse;
import com.skincancerdetection.bffnode.model.RegistrationDto;

public interface CommonServiceRouter {
    CommonResponse registerUser(RegistrationDto registrationDto);
}
