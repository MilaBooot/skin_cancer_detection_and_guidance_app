package com.skincancerdetection.bffnode.router;

import com.skincancerdetection.bffnode.enums.ErrorEnum;
import com.skincancerdetection.bffnode.exception.BffNodeException;
import com.skincancerdetection.bffnode.model.CommonResponse;
import com.skincancerdetection.bffnode.model.ImageProcRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestTemplate;

@Component
public class MlServiceRouterImpl implements MlServiceRouter{
    private static final Logger LOGGER = LoggerFactory.getLogger(MlServiceRouterImpl.class);

    @Autowired
    private RestTemplate restTemplate;

    @Value("${ml.service.url:http://localhost:5001/mlService/predict}")
    private String mlServiceUrl;


    @Override
    public CommonResponse processImage(ImageProcRequest imageProcRequest) {
        ResponseEntity<CommonResponse> responseEntity = null;
        try {
            responseEntity = restTemplate
                    .postForEntity(mlServiceUrl, imageProcRequest, CommonResponse.class);

            if (responseEntity.getStatusCode().value()!= HttpStatus.OK.value()) {
                throw new BffNodeException(responseEntity.getStatusCode().getReasonPhrase()
                        , ErrorEnum.ML_SERVICE_ERROR.getErrMessage()
                        , new RuntimeException());

            }

        } catch (HttpClientErrorException e) {
            LOGGER.error(e.getMessage());
            throw new BffNodeException(e.getMessage(), ErrorEnum.ML_SERVICE_ERROR.getErrMessage(), e);
        }
        return responseEntity.getBody();

    }
}
