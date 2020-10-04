package com.skincancerdetection.bffnode.service;

import com.skincancerdetection.bffnode.model.*;

import java.util.List;

public interface CommonService {
    void registerUser(UserDetailsDto userDetailsDto);
    UserInfoResponseDto retrieveUser(UserInfoRequestDto userInfoRequestDto);
    List<QuestionDto> getQuestionnaire();
    public ImageProcReponse getPrediction(ImageProcRequest imageProcRequest);
    List<DoctorDetailsDto> getDoctors(double longitude, double latitude);
    void uploadDocument(FileUploadDto fileUploadDto);
    List<UserDocuments> getUserDocuments(String username);
    byte[] getFile(String username, String filename);
    void deleteDocument(String username, String filename);
    CancerTypeReponse getCancerDetails(String type);

}
