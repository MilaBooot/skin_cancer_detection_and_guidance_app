package com.skincancerdetection.bffnode.exception;

import lombok.Data;

@Data
public class DuplicateEntryException extends RuntimeException {
    private String errorCode;

    public DuplicateEntryException(String errorCode, String message, Throwable e) {
        super(message, e);
        this.errorCode = errorCode;
    }
    public DuplicateEntryException(String message, Throwable e) {
        super(message, e);
    }

}
