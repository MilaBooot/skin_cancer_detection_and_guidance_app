############################################################################
# Name of file: hackathon_ml_api_wrapper.py
# Description: This is the wrapper file which would do the necessary conversion from BFF
# Revision: 1.0
# Last Update:
# Authors:
#############################################################################

#Global Variables
THRESHOLD = [70, 50] #This determines the threshold for high/medium/low
                     # >70 => HIGH, 50<X<70 => MEDIUM, <50 => LOW


class hackathon_ml_api_wrapper:

    def image_resize (self, bff_input):
        print('To check with Deepak/Shandanu')


    def predict_model (self, bff_input):
        print('Loading the model')

        #Load the model from db/json file
        #return the predicted value

    def compute_risk (self, y_predict, THRESHOLD):
        print ('Computing risk')

        for i in len(y_predict):
            for j in (len(THRESHOLD) - 1):
                if (y_predict[i]>THRESHOLD[j+1]) & (y_predict[i]<THRESHOLD[j]):
                    high.append(i, j)
                elif y_predict[i]>THRESHOLD[j]:
                    medium.append(i, j+1)
                else:
                    low.append(i,0)

        if len(high)!=0 & len(medium)!=0 & len(low)!=0:
            return high, medium, low
        elif len(high)==0 & len(medium)!=0 & len(low)!=0:
            return medium, low
        else:
            return low



