package com.skincancerdetection.bffnode.exception;

import lombok.Data;
import lombok.Getter;

@Data
public class ServiceDownException extends RuntimeException {
    private String errorCode;

    public ServiceDownException(String errorCode, String message, Throwable e) {
        super(message, e);
        this.errorCode = errorCode;
    }
    public ServiceDownException(String message, Throwable e) {
        super(message, e);
    }
}
