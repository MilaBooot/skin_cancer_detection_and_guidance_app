package com.skincancerdetection.bffnode.router;

import com.skincancerdetection.bffnode.model.*;

public interface CommonServiceRouter {
    CommonResponse registerUser(UserDetailsDto userDetailsDto);
    CommonResponse retrieveUser(UserInfoRequestDto userInfoRequestDto);
    CommonResponse getQuestionnaire();
    CommonResponse getDoctors(double longitude, double latitude);
    CommonResponse uploadDocument(FileUploadDto fileUploadDto);
    CommonResponse getUserDocuments(String username);
    CommonResponse getFile(String username, String filename);
    void deleteDocument(String username, String filename);
}
