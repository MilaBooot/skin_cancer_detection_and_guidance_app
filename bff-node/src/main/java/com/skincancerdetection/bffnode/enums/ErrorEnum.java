package com.skincancerdetection.bffnode.enums;

public enum ErrorEnum {
    ENCRYPTION_ERROR("ERR01", "Encryption error"),
    DECRYPTION_ERROR("ERR02", "Decryption error"),
    COMMON_SERVICE_ERROR("ERR03", "Common service down"),
    USER_NOT_FOUND("ERR04", "Incorrect Username or Password"),
    USER_EXISTS_FOUND("ERR04", "User already registered"),
    ML_SERVICE_ERROR("ERR05", "Error occurred in Image processing"),
    UNANSWERED_ERROR("ERR07", "Please complete the questionnaire");


    ErrorEnum(String errCode, String errMessage) {
        this.errCode = errCode;
        this.errMessage = errMessage;
    }

    public String getErrCode() {
        return errCode;
    }

    public String getErrMessage() {
        return errMessage;
    }

    private String errCode;
    private String errMessage;
}
