package com.skincancerdetection.bffnode.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class UserInfoResponseDto {
    private String first_name;
    private String last_name;
    private String password;
    private String dob;
    private String gender;
}
