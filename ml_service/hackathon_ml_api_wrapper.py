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

    def image_resize (self, bff_input, IMAGE_SIZE, IMAGE_DIMENSION):

        image_array = cv2.imread(bff_input)
        image = cv2.resize(image_array, (IMAGE_SIZE, IMAGE_SIZE, IMAGE_DIMENSION))
        return image


    def predict_model (self, image):
        print('Loading the model')

        #Load the model from db/json file
        #return the predicted value
        return y_predict

    def compute_risk_using_image (self, y_predict, THRESHOLD, RISK_LABEL):
        print ('Computing risk')

        if(y_predict[0]>THRESHOLD[0]):
            return RISK_LABEL[0]
        elif (y_predict[0]>THRESHOLD[1]) & (y_predict[0]<THRESHOLD[0]):
            return RISK_LABEL[1]
        elif (y_predict[0]>THRESHOLD[0]) & (y_predict[0]<THRESHOLD[1]):
            return RISK_LABEL[2]
        else:
            return RISK_LABEL[3]

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

    def decision_logic(self, weight, y_predict, RISK_LABEL):
        o_probability = weight * y_predict[0]

        o_result = [math.ceil(o_probability), RISK_LABEL, y_predict[1]]


        return o_result



#call this function for ml_api
def predict_cancer(bff_input, answer, THRESHOLD, RISK_LABEL, IMAGE_SIZE, IMAGE_DIMENSION):
    print ('predicting...')
    print ('creating class handles')
    HMLAPIW = hackathon_ml_api_wrapper()
    
    print ('Resizing input image')
    image = HMLAPIW.image_resize(bff_input=bff_input, IMAGE_SIZE=IMAGE_SIZE, IMAGE_DIMENSION=IMAGE_DIMENSION)
    y_predict = HMLAPIW.predict_model(image=image)
    risk = HMLAPIW.compute_risk_using_image(y_predict=y_predict, THRESHOLD=THRESHOLD, RISK_LABEL=RISK_LABEL)
    weight = HMLAPIW.compute_weight_using_questionarie(answer=answer)
    o_result = HMLAPIW.decision_logic(weight=weight, y_predict=y_predict, RISK_LABEL=risk)













