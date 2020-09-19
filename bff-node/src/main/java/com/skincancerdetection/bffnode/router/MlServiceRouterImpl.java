package com.skincancerdetection.bffnode.router;

import com.skincancerdetection.bffnode.model.ImageProcRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
public class MlServiceRouterImpl implements MlServiceRouter{

    @Autowired
    private RestTemplate restTemplate;

    @Value("${ml.service.url}")
    private String mlServiceUrl;


    @Override
    public void processImage(ImageProcRequest imageProcRequest) {
        //invoke service
        //restTemplate.postForEntity(mlServiceUrl, imageProcRequest,)
    }
}
