############################################################################
# Name of file: hackathon_ml_api_wrapper.py
# Description: This is the wrapper file which would do the necessary conversion from BFF
# Revision: 1.0
# Last Update:
# Authors:
#############################################################################
# Importing python modules
import math
import cv2
import numpy as np
from keras.models import load_model

# Global Variables
THRESHOLD = [70, 50, 10]  # This determines the threshold for high/medium/low
                          # >70 => HIGH, 50<X<70 => MEDIUM, 10<X<50 => LOW, >10 => Not applicable

RISK_LABEL = ['HIGH', 'MEDIUM', 'LOW', 'NOT_APPLICABLE']
CANCER = ['YES', 'NO']
TYPE = ['a', 'b', 'c', 'd', 'e', 'f']
IMAGE_SIZE = 256
IMAGE_DIMENSION = 3

print('Loading the model')
#loaded_model = load_model("C:/Users/kananth2/Downloads/Hackathon_Dataset/temp_model.h5", compile=False)

class hackathon_ml_api_wrapper:

    # Function Description: This function takes user image as input and resizes it as required
    # Function Input: User image
    # Function Output: Resized image
    def image_resize(self, input_image, IMAGE_SIZE, IMAGE_DIMENSION):

        image = cv2.resize(-1, input_image, (IMAGE_SIZE, IMAGE_SIZE, IMAGE_DIMENSION))
        return image

    # Function Description: This function predicts the image using trained ML model
    # Function Input: loaded_model, input image, TYPE
    # Function Output: answer in binary + integer format
    def predict_model(self, loaded_model, input_image, TYPE):

        temp_predictions = loaded_model.predict(input_image)
        y_pred = np.argmax(temp_predictions[0], axis=0) #index of class with highest accuracy
        prediction = [temp_predictions[0][y_pred], TYPE[y_pred]]
        return prediction


    # Function Description: This function converts the input answer (string format) to binary + integer format
    # Function Input: User answer
    # Function Output: answer in binary + integer format
    def convert_answer_string_to_int(self, input_answer):

        #Local variable declaration
        temp_answer = []

        for i in range(0, len(input_answer)):
            if input_answer[i] is 'Yes':
                temp_answer.append(1)
            elif input_answer[i] is 'No':
                temp_answer.append(0)
            elif input_answer[i] is 'Ivorywhite':
                temp_answer.append(2)
            elif input_answer[i] is 'Pale':
                temp_answer.append(3)
            elif input_answer[i] is 'Brown':
                temp_answer.append(4)
            elif input_answer[i] is 'Black':
                temp_answer.append(5)
            elif input_answer[i] is 'Fair':
                temp_answer.append(6)

        return temp_answer


    # Function Description: This function identifies the risk label based on y_predict percentage and threshold value
    # Function Input: y_predict, threshold and risk label
    # Function Output: risk label
    def compute_risk_using_image(self, y_predict, THRESHOLD, RISK_LABEL):

        if (y_predict[0]*100 > THRESHOLD[0]):
            return RISK_LABEL[0]
        elif (y_predict[0]*100 > THRESHOLD[1]) & (y_predict[0]*100 < THRESHOLD[0]):
            return RISK_LABEL[1]
        elif (y_predict[0]*100 > THRESHOLD[0]) & (y_predict[0]*100 < THRESHOLD[1]):
            return RISK_LABEL[2]
        else:
            return RISK_LABEL[3]

    # Function Description: This function identifies the risk using questionarie
    # Function Input: user answer with binary + integer encoding
    # Function Output:  weights
    def compute_weight_using_questionarie(self, answer):

        #Local Variable Declaration
        temp_answer = 1

        for i in answer:  # Bit wise OR
            temp_answer = answer[i] | temp_answer

        if (temp_answer == 1) | (answer[3] & answer[7]):
            weight = 1
        elif ~(answer[3] & answer[5] & answer[7]):
            weight = 0.5
        elif (~answer[3] & answer[5] & answer[7] & answer[9]):
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

    # Function Description: This is the decision logic
    # Function Input: weight, y_predict, RISK LABEL
    # Function Output: list which contains 4 values
    def decision_logic(self, weight, y_predict, RISK_LABEL, CANCER):

        if RISK_LABEL is 'NOT_APPLICABLE':
            temp_cancer = CANCER[1]
        else:
            temp_cancer = CANCER[0]

        o_probability = weight * y_predict[0] * 100

        o_result = {"cancer": temp_cancer, "probability": math.ceil(o_probability),
                    "riskFactor": RISK_LABEL, "type": y_predict[1]}

        return o_result


print('creating class handles')
HMLAPIW = hackathon_ml_api_wrapper()


# Function Description: This function is called by ml_api. It sequences akk the above function calls
# Function Input: weight, y_predict, RISK LABEL
# Function Output: list which contains 4 values
def predict_cancer(input_image, input_answer):
    print('Input image is read and resizing is in progress')
    #image = HMLAPIW.image_resize(input_image=input_image, IMAGE_SIZE=IMAGE_SIZE, IMAGE_DIMENSION=IMAGE_DIMENSION)
    #y_predict = HMLAPIW.predict_model(loaded_model=loaded_model, input_image=image, TYPE=TYPE)
    y_predict = [0.95, 'MELANOMA']
    risk = HMLAPIW.compute_risk_using_image(y_predict=y_predict, THRESHOLD=THRESHOLD, RISK_LABEL=RISK_LABEL)
    answer = HMLAPIW.convert_answer_string_to_int(input_answer=input_answer)
    weight = HMLAPIW.compute_weight_using_questionarie(answer=answer)
    print('Weight is', weight)
    o_result = HMLAPIW.decision_logic(weight=weight, y_predict=y_predict, RISK_LABEL=risk, CANCER=CANCER)
    return o_result

#Sanity check
input_image = []
input_answer = ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes','NO', 'Yes', 'No']
result = predict_cancer(input_image=input_image, input_answer=input_answer)
print(result)
