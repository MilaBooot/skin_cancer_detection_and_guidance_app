########################################################################################################################
# Name of file: hackathon_deep_learning_using_transfer_learning.py
# Description: This file uses transfer learning technique
# Revision: 1.0
# Last Update:
# Authors:
########################################################################################################################

#Importing the important libraries
from tensorflow.python.keras.applications import ResNet50
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras import optimizers
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint

#%matplotlib inline

#Global Variables
DATASETDIR = ''  #Parent directory of videos
IMAGE_SIZE = 256  # Image Size
IMAGE_DIMENSION = 3
CLASS = 7  #This is a multiclass classification problem - has 7 classes
LABEL = [0, 1, 2, 3, 4, 5, 6]
EPOCH = 100
BATCH_SIZE = 100
STEPS_PER_EPOCH_TRAINING = 10  #Training images processed in each step would be no.-of-train-images / STEPS_PER_EPOCH_TRAINING
STEPS_PER_EPOCH_VALIDATION = 10
BATCH_SIZE_TRAINING = 10
BATCH_SIZE_VALIDATION = 10
BATCH_SIZE_TESTING = 10
EARLY_STOP_PATIENCE = 3  #EARLY_STOP_PATIENCE < EPOCH
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

class deep_learning_model_creation:

    def deep_learning_model_creation_using_transfer_learning(self, MODEL_OPTIMIZER, MODEL_LOSS, LOSS_METRICS,
                            RESNET50_POOLING_AVERAGE, FIRST_DENSE_LAYER_ACTIVATION,
                            OUTPUT_LAYER_ACTIVATION, SECOND_DENSE_LAYER_ACTVIVATION,
                            FIRST_DENSE_LAYER_NEURONS, SECOND_DENSE_LAYER_NEURONS):
        model = Sequential()
        model.add(ResNet50(include_top=False, pooling=RESNET50_POOLING_AVERAGE, weights='imagenet'))
        model.add(Dense(FIRST_DENSE_LAYER_NEURONS, activation=FIRST_DENSE_LAYER_ACTIVATION))
        model.add(Dense(SECOND_DENSE_LAYER_NEURONS, activation=SECOND_DENSE_LAYER_ACTVIVATION))
        model.add(Dense(CLASS, activation=OUTPUT_LAYER_ACTIVATION))
        model.layers[0].trainable = False
        model.summary()

        #custom optimizer
        #sgd = optimizers.SGD(lr = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
        model.compile(optimizer=MODEL_OPTIMIZER, loss=MODEL_LOSS, metrics=LOSS_METRICS)
        model.save('transfer_learning.model')

        return model

    def create_data_set(self, IMAGE_SIZE, BATCH_SIZE_TRAINING, CLASS_MODE,
                        BATCH_SIZE_VALIDATION, BATCH_SIZE_TESTING,
                        DATASETDIR, EARLY_STOP_PATIENCE):
        data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)

        train_generator = data_generator.flow_from_directory(
                                                             DATASETDIR + 'Train', 
                                                             target_size=(IMAGE_SIZE, IMAGE_SIZE),
                                                             batch_size=BATCH_SIZE_TRAINING,
                                                             class_mode=CLASS_MODE
                                                             )

        validation_generator = data_generator.flow_from_directory(
                                                                  DATASETDIR + 'Validation',
                                                                  target_size=(IMAGE_SIZE, IMAGE_SIZE),
                                                                  batch_size=BATCH_SIZE_VALIDATION,
                                                                  class_mode=CLASS_MODE
                                                                  )

        test_generator = data_generator.flow_from_directory(
                                                            directory=DATASETDIR + 'Test',
                                                            target_size=(IMAGE_SIZE, IMAGE_SIZE),
                                                            batch_size=BATCH_SIZE_TESTING,
                                                            class_mode=None,
                                                            shuffle=False,
                                                            seed=123
                                                            )

        (BATCH_SIZE_TRAINING, len(train_generator), BATCH_SIZE_VALIDATION, len(validation_generator))

        cb_early_stopper = EarlyStopping(monitor='val_loss', patience=EARLY_STOP_PATIENCE)
        cb_checkpointer = ModelCheckpoint(filepath=DATASETDIR + 'best.hdf5', monitor='val_loss',
                                          save_best_only=True, mode='auto')

        return train_generator, validation_generator, test_generator, cb_early_stopper, cb_checkpointer

    def train_model(self, model, train_generator, STEPS_PER_EPOCH_TRAINING, EPOCH, validation_generator,
                    STEPS_PER_EPOCH_VALIDATION, cb_checkpointer, cb_early_stopper):

        fit_history = model.fit_generator(train_generator, steps_per_epoch=STEPS_PER_EPOCH_TRAINING,
                                          epochs=EPOCH, validation_data=validation_generator,
                                          validation_steps=STEPS_PER_EPOCH_VALIDATION,
                                          callbacks=[cb_checkpointer, cb_early_stopper]
                                          )
        return fit_history, model

    def test_model(self, test_generator, model, NUM_TEST_IMAGES):
        #model = tf.keras.models.load_model('test_model')
        #model.load_weights("../working/best.hdf5")
        test_generator.reset()
        scores = model.predict_generator(test_generator, NUM_TEST_IMAGES)  # 1514 testing images
        print("Accuracy = ", scores[1])

    def predict_model(self, model, predict_image):
        predictions = model.predict_generatot(predict_image, 1)
        y_pred = np.argmax(predictions, axis=1) #index of class with highest accuracy
        print('This module is WIP')
        return predictions[y_pred], y_pred

if __name__ == "__main__":
    print('Creating class handles')
    DLM = deep_learning_model_creation()

    print('Deep learning model creation is in progress - Layer addition is happening')
    created_model = DLM.deep_learning_model_creation_using_transfer_learning(
                                                           MODEL_OPTIMIZER=MODEL_OPTIMIZER, 
                                                           MODEL_LOSS=MODEL_LOSS,
                                                           LOSS_METRICS=LOSS_METRICS,
                                                           RESNET50_POOLING_AVERAGE=RESNET50_POOLING_AVERAGE,
                                                           FIRST_DENSE_LAYER_ACTIVATION=FIRST_DENSE_LAYER_ACTIVATION,
                                                           OUTPUT_LAYER_ACTIVATION=OUTPUT_LAYER_ACTIVATION,
                                                           SECOND_DENSE_LAYER_ACTVIVATION=SECOND_DENSE_LAYER_ACTVIVATION,
                                                           FIRST_DENSE_LAYER_NEURONS=FIRST_DENSE_LAYER_NEURONS,
                                                           SECOND_DENSE_LAYER_NEURONS=SECOND_DENSE_LAYER_NEURONS
                                                           )

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
    #USER_IMAGE= <IMAGE INPUT FROM USER>
    probability, type = DLM.predict_model(model=trained_model, USER_IMAGE=USER_IMAGE)
    
   #####################################################################EOF####################################################################
