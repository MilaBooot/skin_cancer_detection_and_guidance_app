package com.skincancerdetection.bffnode.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class BffNodeController {

    @GetMapping(value="/register")
    public ResponseEntity<String> getUser() {
        return new ResponseEntity<>("Hi", HttpStatus.OK);
    }

}
