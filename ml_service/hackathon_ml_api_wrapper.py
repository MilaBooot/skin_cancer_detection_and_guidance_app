###########################################################################################
# Name of file: hackathon_ml_api_wrapper.py
# Description: This is the wrapper file which acts as interface between ML model and BFF
# Revision: 1.0
# Last Update:
# Authors:
############################################################################################

# Importing python modules
import math
import cv2
import numpy as np
from tensorflow.keras.models import model_from_json, load_model

# Global Variables
THRESHOLD = [70, 50, 10]  # This determines the threshold for high/medium/low
                          # >70 => HIGH, 50<X<70 => MEDIUM, 10<X<50 => LOW, >10 => Not applicable

RISK_LABEL = ['HIGH', 'MEDIUM', 'LOW', 'NOT_APPLICABLE']
CANCER = ['YES', 'NO']
TYPE = ['Actinic_Keratosis', 'Basal_Cell_Carcinoma', 'BKL', 'Dermtofibroma', 'Melanoma', 'Nevus', 'Vascular_Lesion']
IMAGE_SIZE = 256
IMAGE_DIMENSION = 3


json_path = 'model/model.json'
weight_path = 'model/model.h5'
# File path for json model and weights

# Below class is used for loading the saved model

class hackathon_ml_api_wrapper:
    def __init__(self, load=True):
        self.model = None
        self.load_model(json_path, weight_path)

    def load_model(self, json_path, weight_path):
        with open(json_path, 'r') as json_file:
            model_json = json_file.read()
            self.model = model_from_json(model_json)
            self.model.load_weights(weight_path)

    # Function Description: This function takes user image as input and resizes it as required
    # Function Input: User image
    # Function Output: Resized image
    def image_resize(self, input_image, IMAGE_SIZE, IMAGE_DIMENSION):
        temp_image2 = cv2.resize(input_image, (IMAGE_SIZE, IMAGE_SIZE))
        image = temp_image2.reshape(-1, IMAGE_SIZE, IMAGE_SIZE, IMAGE_DIMENSION)
        return image

    # Function Description: This function predicts the image using trained ML model
    # Function Input: loaded_model, input image, TYPE
    # Function Output: answer in binary + integer format
    def predict_model(self, input_image, TYPE):

        print('model.predict function is called')
        temp_prediction = self.model.predict(input_image)
        print('model.predict has predicted')
        print('np.argmax function is called')
        y_pred = np.argmax(temp_prediction[0], axis=0) #index of class with highest accuracy
        print('np.argmax function is complete')
        prediction = [temp_prediction[0][y_pred], TYPE[y_pred]]
        print('temp prediction is ', temp_prediction)
        print('y_pred is ', y_pred)
        return prediction

    # Function Description: This function identifies the risk label based on y_predict percentage and threshold value
    # Function Input: y_predict, threshold and risk label
    # Function Output: risk label
    def compute_risk_using_image(self, y_predict, THRESHOLD, RISK_LABEL):

        if (y_predict[0]*100 > THRESHOLD[0]):
            return RISK_LABEL[0]
        elif (y_predict[0]*100 > THRESHOLD[1]) & (y_predict[0]*100 <= THRESHOLD[0]):
            return RISK_LABEL[1]
        elif (y_predict[0]*100 > THRESHOLD[0]) & (y_predict[0]*100 <= THRESHOLD[1]):
            return RISK_LABEL[2]
        else:
            return RISK_LABEL[3]

    # Function Description: This function identifies the risk using questionnaire
    # Function Input: user answer
    # Function Output: weights
    def compute_weight_using_questionarie(self, answer):

        if (answer[1] is 'Yes') & (answer[3] is 'Yes') & (answer[6] is 'Always burns ,blisters and peels'):
            weight = 1
        elif (answer[0] is 'No') & (answer[2] is 'No') & (answer[5] is 'Yes') & (answer[7] is 'Black')\
            &((answer[6] is 'Often burns,blisters and peels') | (answer[6] is 'Burns moderately')):
            weight = 0.9
        elif (answer[4] is 'Yes') & (answer[6] is 'Burns rarely'):
            weight = 0.3
        elif (answer[4] is 'Yes') & (answer[5] is 'Yes') & (answer[6] is 'Often burns,blisters and peels')\
            & (answer[7] is 'Black'):
            weight = 0.8
        elif (answer[0] is 'Yes') & (answer[1] is 'No') & (answer[2] is 'Yes') & (answer[3] is 'No')\
              & (answer[4] is 'No'):
            weight = 0.2
        elif (answer[7] is 'Ivory white') & (answer[5] is 'Yes') & (answer[6] is 'Burns moderately'):
            weight = 0.7
        elif (answer[7] is 'Fair') & (answer[1] is 'Yes'):
            weight = 0.6
        else:
            weight = 0.1

        return weight

    # Function Description: This is the decision logic
    # Function Input: weight, y_predict, RISK LABEL
    # Function Output: list which contains 4 values
    def decision_logic(self, weight, y_predict, RISK_LABEL, CANCER):

        if RISK_LABEL is 'NOT_APPLICABLE':
            temp_cancer = CANCER[1]
        else:
            temp_cancer = CANCER[0]

        o_probability = ((weight+y_predict[0])/2 )*100

        o_result = {"cancer": temp_cancer, "value": math.ceil(o_probability),
                    "type": y_predict[1], "riskFactor": RISK_LABEL}

        return o_result


    # Function Description: This function is called by ml_api. It sequences akk the above function calls
    # Function Input: weight, y_predict, RISK LABEL
    # Function Output: list which contains 4 values
    def predict_cancer(self, input_image, input_answer):
        #self.model = load_model(weight_path)
        
        print('Input image is read and resizing is in progress')
        image = self.image_resize(input_image=input_image, IMAGE_SIZE=IMAGE_SIZE, IMAGE_DIMENSION=IMAGE_DIMENSION)
        print('Input image is resized as required')

        print('Prediction is in progress')
        y_predict = self.predict_model(input_image=image, TYPE=TYPE)
        print('Risk evaluation using image is in progress')

        risk = self.compute_risk_using_image(y_predict=y_predict, THRESHOLD=THRESHOLD, RISK_LABEL=RISK_LABEL)
        print('Converting input answer to binary+integer format')

        print('compute weight using questionnaire')
        weight = self.compute_weight_using_questionarie(answer=input_answer)
        print('Concatenating result')

        o_result = self.decision_logic(weight=weight, y_predict=y_predict, RISK_LABEL=risk, CANCER=CANCER)
        print('Result is ', o_result)

        return o_result


if __name__ == "__main__":
    # Sanity check
    input_image = 'D:/projects/test.jpeg'
    image = cv2.imread(input_image)
    input_answer = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Burns rarely', 'Fair']
    result = predict_cancer(input_image=image, input_answer=input_answer)

    print(result)


###################################################EOF##################################################################
