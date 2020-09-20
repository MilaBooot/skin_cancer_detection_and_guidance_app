package com.skincancerdetection.bffnode.utils;

import com.skincancerdetection.bffnode.model.QuestionnaireResponse;

import java.util.HashMap;
import java.util.Map;

public class SurveyUtil {
    private static Map<String, QuestionnaireResponse> questionnaireResponseMap = new HashMap<>();

    public static void recordResponse(QuestionnaireResponse response, String userid) {
        questionnaireResponseMap.put(userid, response);
    }
    public static QuestionnaireResponse getResponse(String userid) {
        return questionnaireResponseMap.get(userid);
    }
}
