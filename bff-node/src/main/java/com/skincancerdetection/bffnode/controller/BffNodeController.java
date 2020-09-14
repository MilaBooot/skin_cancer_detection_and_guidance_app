package com.skincancerdetection.bffnode.controller;

import com.skincancerdetection.bffnode.model.RegistrationRequest;
import com.skincancerdetection.bffnode.model.UserDetailsDto;
import com.skincancerdetection.bffnode.service.CommonService;
import org.dozer.DozerBeanMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class BffNodeController {

    @Autowired
    private CommonService commonService;

    @Autowired
    private DozerBeanMapper mapper;

    @PostMapping(value="/register")
    public ResponseEntity registerUser(@RequestBody RegistrationRequest request) {

        UserDetailsDto userDetailsDto = mapper.map(request, UserDetailsDto.class);
        commonService.registerUser(userDetailsDto);
        return new ResponseEntity(HttpStatus.CREATED);
    }

}
