package com.skincancerdetection.bffnode.router;

import com.skincancerdetection.bffnode.model.CommonResponse;
import com.skincancerdetection.bffnode.model.ImageProcRequest;

public interface MlServiceRouter {
     CommonResponse processImage(ImageProcRequest imageProcRequest);
}
