package com.skincancerdetection.bffnode.controller;

import com.skincancerdetection.bffnode.assemble.RequestAssembler;
import com.skincancerdetection.bffnode.model.*;
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

    @Autowired
    private RequestAssembler requestAssembler;

    @PostMapping(value="/register")
    public ResponseEntity registerUser(@RequestBody RegistrationRequest request) {

        UserDetailsDto userDetailsDto = requestAssembler.assembleUserDetailsDto(request);
        commonService.registerUser(userDetailsDto);
        return new ResponseEntity(HttpStatus.CREATED);
    }

    @PostMapping(value="/authenticate")
    public ResponseEntity authenticateUser(@RequestBody AuthenticationRequest request) {

        UserInfoRequestDto userInfoRequestDto = requestAssembler.assembleUserInfoRequestDto(request);
        UserInfoResponseDto userInfoResponseDto = commonService.retrieveUser(userInfoRequestDto);

        AuthenticationResponse response = requestAssembler
                .assembleAuthenticationResponse(userInfoResponseDto, request.getUsername());

        if (userInfoResponseDto.getPassword().equalsIgnoreCase(request.getPassword())) {
            return new ResponseEntity(response, HttpStatus.OK);
        }
        return new ResponseEntity(HttpStatus.NOT_FOUND);

    }

}
