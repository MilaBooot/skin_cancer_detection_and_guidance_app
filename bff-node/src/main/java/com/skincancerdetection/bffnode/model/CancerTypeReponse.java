package com.skincancerdetection.bffnode.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class CancerTypeReponse {
    private String type;
    private String description;
    private List<String> symptoms;
    private List<String> riskFactor;
    private String link;
}
