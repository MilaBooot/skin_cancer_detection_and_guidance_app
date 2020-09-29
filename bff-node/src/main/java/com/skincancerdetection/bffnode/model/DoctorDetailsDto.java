package com.skincancerdetection.bffnode.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class DoctorDetailsDto {
    private String name;
    private String speciality;
    private String hospital;
    public double latitude;
    public double longitude;
}
