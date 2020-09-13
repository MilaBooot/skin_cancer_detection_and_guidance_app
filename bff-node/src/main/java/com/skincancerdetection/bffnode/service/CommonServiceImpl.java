package com.skincancerdetection.bffnode.service;

import com.skincancerdetection.bffnode.model.RegistrationDto;
import com.skincancerdetection.bffnode.router.CommonServiceRouter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CommonServiceImpl implements CommonService{

    @Autowired
    private CommonServiceRouter commonServiceRouter;

    @Override
    public void registerUser(RegistrationDto registrationDto) {
        commonServiceRouter.registerUser(registrationDto);
    }

}
