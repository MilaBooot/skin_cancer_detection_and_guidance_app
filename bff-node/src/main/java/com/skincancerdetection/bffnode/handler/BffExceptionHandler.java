package com.skincancerdetection.bffnode.handler;

import com.skincancerdetection.bffnode.exception.BffNodeException;
import com.skincancerdetection.bffnode.exception.DuplicateEntryException;
import com.skincancerdetection.bffnode.model.CommonResponse;
import com.skincancerdetection.bffnode.model.ErrorMessageDto;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class BffExceptionHandler {

    @ExceptionHandler(value = DuplicateEntryException.class)
    @ResponseStatus(value = HttpStatus.CONFLICT)
    public String handleDuplicateException(DuplicateEntryException ex) {
        return getErrorReponse(ex);
    }

    @ExceptionHandler(value = BffNodeException.class)
    @ResponseStatus(value = HttpStatus.INTERNAL_SERVER_ERROR)
    public String handleBffNodeException(BffNodeException ex) {
        return getErrorReponse(ex);
    }


    private String getErrorReponse(RuntimeException ex) {
        return ex.getMessage();
    }
}
