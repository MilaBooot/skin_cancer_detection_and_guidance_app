############################################################################
# Name of file: hackathon_top_file.py
# Description: This is the top file
# Revision: 1.0
# Last Update:
# Authors:
#############################################################################

#Importing user defined modules
from hackathon_create_data_set import data_set_creation as DSC
from hackathon_deep_learning_model import deep_learning_model_creation as DLMC
from hackathon_deep_learning_using_transfer_learning import deep_learning_model_creation as DLM

#Global Variables
DATASETDIR = ''  # Parent directory of videos
IMAGE_SIZE = 256  # Image Size
IMAGE_DIMENSION = 3
CLASS = 9  # This is a multiclass classification problem - has 7 classes
LABEL = [0, 1, 2, 3, 4, 5, 6]
EPOCH = 1
BATCH_SIZE = 1
STEPS_PER_EPOCH_TRAINING = 1  #Training images processed in each step would be no. of train images/STEPS_PER_EPOCH_TRAINING
STEPS_PER_EPOCH_VALIDATION = 1
BATCH_SIZE_TRAINING = 1
BATCH_SIZE_VALIDATION = 1
BATCH_SIZE_TESTING = 1
EARLY_STOP_PATIENCE = 3 #EARLY_STOP_PATIENCE < EPOCH
NUM_TEST_IMAGES = 10

#Deep Learning Variables
CLASS_MODE = 'categorical'
MODEL_OPTIMIZER = 'adam'
MODEL_LOSS = 'categorical_crossentropy'
MODEL_METRICS = 'accuracy'
LOSS_METRICS = ['accuracy']  #Common accuracy metric for all outputs, but can use different metrics for different output
RESNET50_POOLING_AVERAGE = 'avg'
FIRST_DENSE_LAYER_ACTIVATION = 'relu'
SECOND_DENSE_LAYER_ACTVIVATION = 'relu'
OUTPUT_LAYER_ACTIVATION = 'softmax'
FIRST_DENSE_LAYER_NEURONS = 1024
SECOND_DENSE_LAYER_NEURONS = 512

class hackathon_skin_cancer_detection_top:

    # Function Description: This function is for sequencing function calls
    # Function Input: filters, stage, block
    # Function Output:
    def sequencing_function_call(self, DATASETDIR, LABEL, IMAGE_SIZE, IMAGE_DIMENSION, CLASS, EPOCH, BATCH_SIZE,
                                 MODEL_OPTIMIZER, MODEL_LOSS, MODEL_METRICS, OUTPUT_LAYER_ACTIVATION, LOSS_METRICS,
                                 RESNET50_POOLING_AVERAGE, FIRST_DENSE_LAYER_ACTIVATION, SECOND_DENSE_LAYER_ACTVIVATION,
                                 FIRST_DENSE_LAYER_NEURONS, SECOND_DENSE_LAYER_NEURONS, CLASS_MODE, BATCH_SIZE_TRAINING,
                                 BATCH_SIZE_VALIDATION, BATCH_SIZE_TESTING, EARLY_STOP_PATIENCE, STEPS_PER_EPOCH_TRAINING,
                                 STEPS_PER_EPOCH_VALIDATION, NUM_TEST_IMAGES
                                 ):

        #X_train, y_train = DSC.create_data_set(DATASETDIR=DATASETDIR, LABEL=LABEL, IMAGE_SIZE=IMAGE_SIZE)
        #print('Train data set is created')

        #DLMC.ResNet50(input_shape=(IMAGE_SIZE, IMAGE_SIZE, IMAGE_DIMENSION), classes=CLASS, X_train=X_train,
        #              y_train=y_train, EPOCH=EPOCH, BATCH_SIZE=BATCH_SIZE, MODEL_OPTIMIZER=MODEL_OPTIMIZER,
        #              MODEL_LOSS=MODEL_LOSS, MODEL_METRICS=MODEL_METRICS, OUTPUT_LAYER_ACTIVATION=OUTPUT_LAYER_ACTIVATION)

        print('Deep learning model creation is in progress - Layer addition is happening')
        created_model = DLM.deep_learning_model_creation_using_transfer_learning(MODEL_OPTIMIZER=MODEL_OPTIMIZER,
                                                                                 MODEL_LOSS=MODEL_LOSS,
                                                                                 LOSS_METRICS=LOSS_METRICS,
                                                                                 RESNET50_POOLING_AVERAGE=RESNET50_POOLING_AVERAGE,
                                                                                 FIRST_DENSE_LAYER_ACTIVATION=FIRST_DENSE_LAYER_ACTIVATION,
                                                                                 OUTPUT_LAYER_ACTIVATION=OUTPUT_LAYER_ACTIVATION,
                                                                                 SECOND_DENSE_LAYER_ACTVIVATION=SECOND_DENSE_LAYER_ACTVIVATION,
                                                                                 FIRST_DENSE_LAYER_NEURONS=FIRST_DENSE_LAYER_NEURONS,
                                                                                 SECOND_DENSE_LAYER_NEURONS=SECOND_DENSE_LAYER_NEURONS)

        print('Train/Validation/Test data generation is in progress')
        train_generator, validation_generator, test_generator, cb_checkpointer, cb_early_stopper = DLM.create_data_set \
            (IMAGE_SIZE=IMAGE_SIZE, BATCH_SIZE_TRAINING=BATCH_SIZE_TRAINING, CLASS_MODE=CLASS_MODE,
             BATCH_SIZE_VALIDATION=BATCH_SIZE_VALIDATION, BATCH_SIZE_TESTING=BATCH_SIZE_TESTING,
             DATASETDIR=DATASETDIR, EARLY_STOP_PATIENCE=EARLY_STOP_PATIENCE)

        print('Deep learning model is in progress')
        fit_history, trained_model = DLM.train_model(model=created_model, train_generator=train_generator,
                                                     STEPS_PER_EPOCH_TRAINING=STEPS_PER_EPOCH_TRAINING, EPOCH=EPOCH,
                                                     validation_generator=validation_generator,
                                                     STEPS_PER_EPOCH_VALIDATION=STEPS_PER_EPOCH_VALIDATION,
                                                     cb_checkpointer=cb_checkpointer, cb_early_stopper=cb_early_stopper)

        print('Time to test your model')
        DLM.test_model(test_generator=test_generator, model=trained_model, NUM_TEST_IMAGES=NUM_TEST_IMAGES)

        print('Time to predict your model')
        #USER_IMAGE = user image path
        probability, type = DLM.predict_model(model=trained_model, predict_image=USER_IMAGE)
        print('Congratulations - Deep learning model is created ')


if __name__ == "__main__":

    DSC = DSC()
    DLMC = DLMC()
    DLM = DLM()

    HSCD_TOP = hackathon_skin_cancer_detection_top()
    HSCD_TOP.sequencing_function_call(DATASETDIR=DATASETDIR, LABEL=LABEL, IMAGE_SIZE=IMAGE_SIZE,
                                      IMAGE_DIMENSION=IMAGE_DIMENSION, CLASS=CLASS, EPOCH=EPOCH, BATCH_SIZE=BATCH_SIZE,
                                      MODEL_LOSS=MODEL_LOSS, MODEL_METRICS=MODEL_METRICS,
                                      OUTPUT_LAYER_ACTIVATION=OUTPUT_LAYER_ACTIVATION, MODEL_OPTIMIZER=MODEL_OPTIMIZER,
                                      LOSS_METRICS=LOSS_METRICS,
                                      RESNET50_POOLING_AVERAGE=RESNET50_POOLING_AVERAGE,
                                      FIRST_DENSE_LAYER_ACTIVATION=FIRST_DENSE_LAYER_ACTIVATION,
                                      SECOND_DENSE_LAYER_ACTVIVATION=SECOND_DENSE_LAYER_ACTVIVATION,
                                      FIRST_DENSE_LAYER_NEURONS=FIRST_DENSE_LAYER_NEURONS,
                                      SECOND_DENSE_LAYER_NEURONS=SECOND_DENSE_LAYER_NEURONS, CLASS_MODE=CLASS_MODE,
                                      BATCH_SIZE_TRAINING=BATCH_SIZE_TRAINING, BATCH_SIZE_VALIDATION=BATCH_SIZE_VALIDATION,
                                      BATCH_SIZE_TESTING=BATCH_SIZE_TESTING, EARLY_STOP_PATIENCE=EARLY_STOP_PATIENCE,
                                      STEPS_PER_EPOCH_TRAINING=STEPS_PER_EPOCH_TRAINING,
                                      STEPS_PER_EPOCH_VALIDATION=STEPS_PER_EPOCH_VALIDATION, NUM_TEST_IMAGES=NUM_TEST_IMAGES)
