############################################################################
# Name of file: hackathon_ml_api_wrapper.py
# Description: This is the wrapper file which would do the necessary conversion from BFF
# Revision: 1.0
# Last Update:
# Authors:
#############################################################################
#Importing python modules
import math
import cv2
import numpy as np

#Global Variables
THRESHOLD = [70, 50, 10] #This determines the threshold for high/medium/low
                         # >70 => HIGH, 50<X<70 => MEDIUM, 10<X<50 => LOW, >10 => Not applicable

RISK_LABEL = ['HIGH', 'MEDIUM', 'LOW', 'NOT_APPLICABLE']
IMAGE_SIZE = 256
IMAGE_DIMENSION = 3

class hackathon_ml_api_wrapper:
  
    #Function Description: This function takes user image as input and resizes it as required
    #Function Input: User image
    #Function Output: Resized image
    def image_resize (self, bff_input, IMAGE_SIZE, IMAGE_DIMENSION):
        
        image = cv2.resize(-1, image_array, (IMAGE_SIZE, IMAGE_SIZE, IMAGE_DIMENSION))
        return image
      
    #Function Description: This function identifies the risk label based on y_predict percentage and threshold value
    #Function Input: y_predict, threshold and risk label
    #Function Output: risk label
    def compute_risk_using_image (self, y_predict, THRESHOLD, RISK_LABEL):

      if(y_predict[0]>THRESHOLD[0]):
            return RISK_LABEL[0]
        elif (y_predict[0]>THRESHOLD[1]) & (y_predict[0]<THRESHOLD[0]):
            return RISK_LABEL[1]
        elif (y_predict[0]>THRESHOLD[0]) & (y_predict[0]<THRESHOLD[1]):
            return RISK_LABEL[2]
        else:
            return RISK_LABEL[3]
      
    #Function Description: This function identifies the risk using questionarie
    #Function Input: questionarie
    #Function Output:  weights
    def compute_weight_using_questionarie(self, answer):

        #Local Variable Definition
        temp_answer = 0
        weight = 1.0

        for i in len(answer) -1: #Bit wise OR
            temp_answer = answer[i] | temp_answer

        if(temp_answer==1) | (answer[3] & answer[7]):
            weight = 1
        elif ~(answer[3] & answer[5] & answer[7]):
            weight = 0.5
        elif  (~answer[3] & answer[5] & answer[7] & answer[9]):
            weight = 0.8
        elif (answer[3] & answer[9]):
            weight = 0.9
        elif (answer[3]):
            weight = 0.75
        elif (temp_answer==0):
            weight = 0.25
        else:
            weight = 0.20
        return weight
      
    #Function Description: This is the decision logic
    #Function Input: weight, y_predict, RISK LABEL
    #Function Output: list which contains 4 values
    def decision_logic(self, weight, y_predict, RISK_LABEL):
        
        if RISK_LABEL=='NOT_APPLICABLE':
            temp_cancer = 'NO'
        else:
            temp_cancer = 'YES'
          
        o_probability = weight * y_predict[0]
    
        o_result = [temp_cancer, math.ceil(o_probability), RISK_LABEL, y_predict[1]]

        return o_result

print ('creating class handles')
HMLAPIW = hackathon_ml_api_wrapper()

#Function Description: This function is called by ml_api. It sequences akk the above function calls
#Function Input: weight, y_predict, RISK LABEL
#Function Output: list which contains 4 values
def predict_cancer(input_image, input_answer):
  
    print ('Input image is read and resizing is in progress')
    image = HMLAPIW.image_resize(bff_input=input_image, IMAGE_SIZE=IMAGE_SIZE, IMAGE_DIMENSION=IMAGE_DIMENSION)
    y_predict = HMLAPIW.predict_model(image=image)
    risk = HMLAPIW.compute_risk_using_image(y_predict=y_predict, THRESHOLD=THRESHOLD, RISK_LABEL=RISK_LABEL)
    weight = HMLAPIW.compute_weight_using_questionarie(answer=input_answer)
    o_result = HMLAPIW.decision_logic(weight=weight, y_predict=y_predict, RISK_LABEL=risk, )
    
    return o_result













