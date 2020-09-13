package com.skincancerdetection.bffnode.controller;

import com.skincancerdetection.bffnode.model.RegistrationDto;
import com.skincancerdetection.bffnode.service.CommonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
public class BffNodeController {

    @Autowired
    private CommonService commonService;

    @PostMapping(value="/register")
    public ResponseEntity registerUser(@RequestBody RegistrationDto registrationDto) {
        commonService.registerUser(registrationDto);
        return new ResponseEntity(HttpStatus.CREATED);
    }

}
