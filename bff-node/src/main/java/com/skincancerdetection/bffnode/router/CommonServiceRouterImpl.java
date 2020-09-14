package com.skincancerdetection.bffnode.router;

import com.skincancerdetection.bffnode.enums.ErrorEnum;
import com.skincancerdetection.bffnode.exception.DuplicateEntryException;
import com.skincancerdetection.bffnode.exception.ServiceDownException;
import com.skincancerdetection.bffnode.model.CommonResponse;
import com.skincancerdetection.bffnode.model.ErrorMessageDto;
import com.skincancerdetection.bffnode.model.UserDetailsDto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
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
        ResponseEntity<CommonResponse> responseEntity = restTemplate
                .postForEntity(url, userDetailsDto, CommonResponse.class);

        if (responseEntity.getStatusCode() == HttpStatus.INTERNAL_SERVER_ERROR) {
            throw new ServiceDownException(responseEntity.getStatusCode().getReasonPhrase()
                    , ErrorEnum.COMMON_SERVICE_ERROR.getErrMessage()
                    , new RuntimeException());

        } else if (responseEntity.getStatusCode() == HttpStatus.CONFLICT) {
            CommonResponse<ErrorMessageDto> response = (CommonResponse<ErrorMessageDto>)responseEntity.getBody().getResult();
            throw new DuplicateEntryException(responseEntity.getStatusCode().getReasonPhrase()
                    , response.getResult().getError()
                    , new RuntimeException());
        }
        return responseEntity.getBody();

    }
}
