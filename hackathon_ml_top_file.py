############################################################################
# Name of file: hackathon_ml_top_file.py
# Description: This is the top file
# Revision: 1.0
# Last Update:
# Authors:
#############################################################################

#Global Variables
DATASETDIR = <Your local path>'  #Parent directory of videos
IMAGE_SIZE = 256  #Image Size
IMAGE_DIMENSION = 3
LABEL = [0, 1, 2, 3, 4, 5, 6, 7, 8]
CLASS = 9 #This is a multiclass classification problem - has 9 classes
EPOCH = 1
BATCH_SIZE = 1

#Deep Learning Variables
MODEL_OPTIMIZER = 'adam'
MODEL_LOSS = 'categorical_crossentropy'
MODEL_METRICS = 'accuracy'
OUTPUT_LAYER_ACTIVATION = 'softmax'

#Importing user defined modules
from Hackathon_create_data_set import data_set_creation as DSC
from ml_api_top import deep_learning_model_creation as DLMC

class hackathon_skin_cancer_detection_top:

    # Function Description: This function is for sequencing function calls
    # Function Input: filters, stage, block
    # Function Output:
    def sequencing_function_call(self, DATASETDIR, LABEL, IMAGE_SIZE, IMAGE_DIMENSION, CLASS, EPOCH, BATCH_SIZE,
                                 MODEL_OPTIMIZER, MODEL_LOSS, MODEL_METRICS, OUTPUT_LAYER_ACTIVATION):

        X_train, y_train = DSC.create_data_set(DATASETDIR=DATASETDIR, LABEL=LABEL, IMAGE_SIZE=IMAGE_SIZE)
        print('Train data set is created')

        DLMC.ResNet50(input_shape=(IMAGE_SIZE, IMAGE_SIZE, IMAGE_DIMENSION), classes=CLASS, X_train=X_train,
                      y_train=y_train, EPOCH=EPOCH, BATCH_SIZE=BATCH_SIZE, MODEL_OPTIMIZER=MODEL_OPTIMIZER,
                      MODEL_LOSS=MODEL_LOSS, MODEL_METRICS=MODEL_METRICS, OUTPUT_LAYER_ACTIVATION=OUTPUT_LAYER_ACTIVATION)
        print('Congratulations - Deep learning model is created ')


if __name__ == "__main__":

    DSC = DSC()
    DLMC = DLMC()

    HSCD_TOP = hackathon_skin_cancer_detection_top()
    HSCD_TOP.sequencing_function_call(DATASETDIR=DATASETDIR, LABEL=LABEL, IMAGE_SIZE=IMAGE_SIZE,
                                      IMAGE_DIMENSION=IMAGE_DIMENSION, CLASS=CLASS, EPOCH=EPOCH, BATCH_SIZE=BATCH_SIZE,
                                      MODEL_OPTIMIZER=MODEL_OPTIMIZER, MODEL_LOSS=MODEL_LOSS, MODEL_METRICS=MODEL_METRICS,
                                      OUTPUT_LAYER_ACTIVATION=OUTPUT_LAYER_ACTIVATION)
