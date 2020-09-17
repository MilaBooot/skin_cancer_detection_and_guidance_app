package com.skincancerdetection.bffnode.assemble;

import com.skincancerdetection.bffnode.model.*;
import org.springframework.stereotype.Component;

@Component
public class RequestAssembler {

    public UserInfoRequestDto assembleUserInfoRequestDto(AuthenticationRequest request) {
        UserInfoRequestDto userInfoRequestDto = new UserInfoRequestDto();
        userInfoRequestDto.setUser_id(request.getUsername());
        return userInfoRequestDto;
    }

    public UserDetailsDto assembleUserDetailsDto(RegistrationRequest request) {
        UserDetailsDto userDetailsDto = new UserDetailsDto();
        userDetailsDto.setDob(request.getDob());
        userDetailsDto.setFirst_name(request.getFirstname());
        userDetailsDto.setLast_name(request.getLastname());
        //TODO: do encryption
        userDetailsDto.setPassword(request.getPassword());
        userDetailsDto.setUser_id(request.getUsername());
        return userDetailsDto;
    }

    public AuthenticationResponse assembleAuthenticationResponse(UserInfoResponseDto userInfoResponseDto
            , String username) {
        AuthenticationResponse response = new AuthenticationResponse();
        response.setFirstname(userInfoResponseDto.getFirst_name());
        response.setLastname(userInfoResponseDto.getLast_name());
        response.setUsername(username);
        return response;
    }
}
