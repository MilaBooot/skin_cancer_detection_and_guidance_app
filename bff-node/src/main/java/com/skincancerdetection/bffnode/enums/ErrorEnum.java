package com.skincancerdetection.bffnode.enums;

public enum ErrorEnum {
    ENCRYPTION_ERROR("ERR01", "Encryption error"),
    DECRYPTION_ERROR("ERR02", "Decryption error");

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
