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
    public CommonResponse handleDuplicateException(DuplicateEntryException ex) {
        return getErrorReponse(ex);
    }

    @ExceptionHandler(value = BffNodeException.class)
    @ResponseStatus(value = HttpStatus.INTERNAL_SERVER_ERROR)
    public CommonResponse handleBffNodeException(BffNodeException ex) {
        return getErrorReponse(ex);
    }


    private CommonResponse getErrorReponse(RuntimeException ex) {
        ErrorMessageDto messageDto = new ErrorMessageDto(ex.getMessage());
        CommonResponse<ErrorMessageDto> response = new CommonResponse(messageDto);
        return response;
    }
}
