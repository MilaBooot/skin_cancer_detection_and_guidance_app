package com.skincancerdetection.bffnode.router;

import com.skincancerdetection.bffnode.enums.ErrorEnum;
import com.skincancerdetection.bffnode.exception.BffNodeException;
import com.skincancerdetection.bffnode.exception.DuplicateEntryException;
import com.skincancerdetection.bffnode.model.CommonResponse;
import com.skincancerdetection.bffnode.model.ErrorMessageDto;
import com.skincancerdetection.bffnode.model.UserDetailsDto;
import com.skincancerdetection.bffnode.model.UserInfoRequestDto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestTemplate;

@Component
public class CommonServiceRouterImpl implements CommonServiceRouter{

    @Value("${common.service.url}")
    private String commonServiceUrl;

    @Value("${common.service.user.registration.endpoint}")
    private String userRegistrationEndpoint;

    @Value("${common.service.user.retrieve.endpoint}")
    private String userRetrieveEndpoint;

    @Autowired
    private RestTemplate restTemplate;

    @Override
    public CommonResponse registerUser(UserDetailsDto userDetailsDto) {
        final String url = new StringBuilder(commonServiceUrl).append(userRegistrationEndpoint).toString();
        ResponseEntity<CommonResponse> responseEntity = null;

        try {
            responseEntity = restTemplate
                    .postForEntity(url, userDetailsDto, CommonResponse.class);

           if (responseEntity.getStatusCode().value()!= HttpStatus.OK.value()) {
                throw new BffNodeException(responseEntity.getStatusCode().getReasonPhrase()
                        , ErrorEnum.COMMON_SERVICE_ERROR.getErrMessage()
                        , new RuntimeException());

            }

        } catch (HttpClientErrorException e) {

            if (e.getStatusCode().value()== HttpStatus.CONFLICT.value()) {
                throw new DuplicateEntryException(e.getStatusCode().getReasonPhrase()
                        , e.getMessage()
                        , new RuntimeException());

            }

            throw new BffNodeException(e.getMessage(), e);
        }
        return responseEntity.getBody();

    }

    @Override
    public CommonResponse retrieveUser(UserInfoRequestDto userInfoRequestDto) {
        final String url = new StringBuilder(commonServiceUrl).append(userRetrieveEndpoint).toString();
        ResponseEntity<CommonResponse> responseEntity = null;
        try {
            responseEntity = restTemplate
                    .postForEntity(url, userInfoRequestDto, CommonResponse.class);

            if (responseEntity.getStatusCode().value()!= HttpStatus.OK.value()) {
                throw new BffNodeException(responseEntity.getStatusCode().getReasonPhrase()
                        , ErrorEnum.COMMON_SERVICE_ERROR.getErrMessage()
                        , new RuntimeException());

            }

        } catch (HttpClientErrorException e) {
            throw new BffNodeException(e.getMessage(), e);
        }
        return responseEntity.getBody();

    }
}
