package com.skincancerdetection.bffnode.exception;

import lombok.Data;

@Data
public class BffNodeException extends RuntimeException {
    private String errorCode;

    public BffNodeException(String errorCode, String message, Throwable e) {
        super(message, e);
        this.errorCode = errorCode;
    }
    public BffNodeException(String message, Throwable e) {
        super(message, e);
    }

}
