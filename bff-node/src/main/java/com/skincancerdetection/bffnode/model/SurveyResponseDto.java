package com.skincancerdetection.bffnode.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class SurveyResponseDto {
    private int id;
    private String answer;
}
