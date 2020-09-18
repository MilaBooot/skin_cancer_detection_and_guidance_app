########################################################################################################################
# Name of file: hackathon_deep_learning_model.py
# Description: This file develops the CNN and deep learning layers
# Revision: 1.0
# Last Update:
# Authors:
########################################################################################################################

#Importing python modules
from keras import layers
from keras.layers import Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, \
    AveragePooling2D, MaxPooling2D, GlobalMaxPooling2D
from keras.models import Model, load_model
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras.applications.imagenet_utils import preprocess_input
import pydot
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
#from resnets_utils import *
from keras.initializers import glorot_uniform
import scipy.misc
from matplotlib.pyplot import imshow
import keras.backend as K
from Hackathon_create_data_set import data_set_creation as DSC

#Global Variables
DATASETDIR = '<Your local path>'  #Parent directory of videos
IMAGE_SIZE = 256  #Image Size
IMAGE_DIMENSION = 3
CLASS = 9 #This is a multiclass classification problem - has 9 classes
LABEL = [0, 1, 2, 3, 4, 5, 6, 7, 8]
EPOCH = 25
BATCH_SIZE = 100

#Deep Learning Variables
MODEL_OPTIMIZER = 'adam'
MODEL_LOSS = 'categorical_crossentropy'
MODEL_METRICS = 'accuracy'
OUTPUT_LAYER_ACTIVATION = 'softmax'

#Global Definitions
K.set_image_data_format('channels_last')
K.set_learning_phase(1)

class deep_learning_model_creation:

    #Function Description: Identity Block
    #Function Input: filters, stage, block
    #Function Output:
    def identity_block(self, X, f, filters, stage, block):

        conv_name_base = 'res' + str(stage) + block + '_branch'
        bn_name_base = 'bn' + str(stage) + block + '_branch'

        #Retrieve Filters
        F1, F2, F3 = filters

        #Save the input value. You'll need this later to add back to the main path.
        X_shortcut = X

        #First component of main path
        X = Conv2D(filters=F1, kernel_size=(1, 1), strides=(1, 1), padding='valid', name=conv_name_base + '2a',
                   kernel_initializer=glorot_uniform(seed=0))(X)
        X = BatchNormalization(axis=3, name=bn_name_base + '2a')(X)
        X = Activation('relu')(X)

        #Second component of main path
        X = Conv2D(filters=F2, kernel_size=(f, f), strides=(1, 1), padding='same', name=conv_name_base + '2b',
                   kernel_initializer=glorot_uniform(seed=0))(X)
        X = BatchNormalization(axis=3, name=bn_name_base + '2b')(X)
        X = Activation('relu')(X)

        #Third component of main path (≈2 lines)
        X = Conv2D(filters=F3, kernel_size=(1, 1), strides=(1, 1), padding='valid', name=conv_name_base + '2c',
                   kernel_initializer=glorot_uniform(seed=0))(X)
        X = BatchNormalization(axis=3, name=bn_name_base + '2c')(X)

        #Final step: Add shortcut value to main path, and pass it through a RELU activation)
        X = Add()([X, X_shortcut])
        X = Activation('relu')(X)

        return X
    #Function Description: filter stage block
    #Function Input:
    #Function Output:
    def convolutional_block(self, X, f, filters, stage, block, s=2):

        #defining name basis
        conv_name_base = 'res' + str(stage) + block + '_branch'
        bn_name_base = 'bn' + str(stage) + block + '_branch'

        #Retrieve Filters
        F1, F2, F3 = filters

        #Save the input value
        X_shortcut = X

        ##### MAIN PATH #####
        #First component of main path
        X = Conv2D(F1, (1, 1), strides=(s, s), name=conv_name_base + '2a', kernel_initializer=glorot_uniform(seed=0))(X)
        X = BatchNormalization(axis=3, name=bn_name_base + '2a')(X)
        X = Activation('relu')(X)

        #Second component of main path
        X = Conv2D(filters=F2, kernel_size=(f, f), strides=(1, 1), padding='same', name=conv_name_base + '2b',
               kernel_initializer=glorot_uniform(seed=0))(X)
        X = BatchNormalization(axis=3, name=bn_name_base + '2b')(X)
        X = Activation('relu')(X)

        #Third component of main path
        X = Conv2D(filters=F3, kernel_size=(1, 1), strides=(1, 1), padding='valid', name=conv_name_base + '2c',
               kernel_initializer=glorot_uniform(seed=0))(X)
        X = BatchNormalization(axis=3, name=bn_name_base + '2c')(X)

        ##### SHORTCUT PATH ####
        X_shortcut = Conv2D(filters=F3, kernel_size=(1, 1), strides=(s, s), padding='valid', name=conv_name_base + '1',
                        kernel_initializer=glorot_uniform(seed=0))(X_shortcut)
        X_shortcut = BatchNormalization(axis=3, name=bn_name_base + '1')(X_shortcut)

        #Final step: Add shortcut value to main path, and pass it through a RELU activation (≈2 lines)
        X = Add()([X, X_shortcut])
        X = Activation('relu')(X)

        return X

    #Function Description: Resnet model
    #Function Input: Input shape, classes, X_train and y_train
    #Function Output:
    def ResNet50(self, input_shape, classes, X_train, y_train, EPOCH, BATCH_SIZE,
                 MODEL_OPTIMIZER, MODEL_LOSS, MODEL_METRICS, OUTPUT_LAYER_ACTIVATION):

        #Define the input as a tensor with shape input_shape
        X_input = Input(input_shape)

        #Zero-Padding
        X = ZeroPadding2D((3, 3))(X_input)

        #Stage 1
        X = Conv2D(64, (7, 7), strides=(2, 2), name='conv1', kernel_initializer=glorot_uniform(seed=0))(X)
        X = BatchNormalization(axis=3, name='bn_conv1')(X)
        X = Activation('relu')(X)
        X = MaxPooling2D((3, 3), strides=(2, 2))(X)

        #Stage 2
        X = DLMC.convolutional_block(X, f=3, filters=[64, 64, 256], stage=2, block='a', s=1)
        X = DLMC.identity_block(X, 3, [64, 64, 256], stage=2, block='b')
        X = DLMC.identity_block(X, 3, [64, 64, 256], stage=2, block='c')

        #Stage 3
        X = DLMC.convolutional_block(X, f=3, filters=[128, 128, 512], stage=3, block='a', s=2)
        X = DLMC.identity_block(X, 3, [128, 128, 512], stage=3, block='b')
        X = DLMC.identity_block(X, 3, [128, 128, 512], stage=3, block='c')
        X = DLMC.identity_block(X, 3, [128, 128, 512], stage=3, block='d')

        #Stage 4
        X = DLMC.convolutional_block(X, f=3, filters=[256, 256, 1024], stage=4, block='a', s=2)
        X = DLMC.identity_block(X, 3, [256, 256, 1024], stage=4, block='b')
        X = DLMC.identity_block(X, 3, [256, 256, 1024], stage=4, block='c')
        X = DLMC.identity_block(X, 3, [256, 256, 1024], stage=4, block='d')
        X = DLMC.identity_block(X, 3, [256, 256, 1024], stage=4, block='e')
        X = DLMC.identity_block(X, 3, [256, 256, 1024], stage=4, block='f')

        #Stage 5
        X = DLMC.convolutional_block(X, f=3, filters=[512, 512, 2048], stage=5, block='a', s=2)
        X = DLMC.identity_block(X, 3, [512, 512, 2048], stage=5, block='b')
        X = DLMC.identity_block(X, 3, [512, 512, 2048], stage=5, block='c')

        #AVGPOOL
        X = AveragePooling2D((2, 2), name="avg_pool")(X)

        #Output layer
        X = Flatten()(X)
        X = Dense(classes, activation=OUTPUT_LAYER_ACTIVATION, name='fc' + str(classes), kernel_initializer=glorot_uniform(seed=0))(X)

        #Create model
        model = Model(inputs=X_input, outputs=X, name='ResNet50')
        model.compile(optimizer=MODEL_OPTIMIZER, loss=MODEL_LOSS, metrics=[MODEL_METRICS])
        model.fit(X_train, y_train, epochs=EPOCH, batch_size=BATCH_SIZE)


#print('Comment below two lines if you are running this file independently, uncomment below line if you are running from top file')
print('Creating class handle')
DLMC = deep_learning_model_creation()

if __name__ == "__main__":

    #print('Use below code only if you are running this file independently')
    #print('Creating class handles for classes')
    #DSC = DSC()
    #DLMC = deep_learning_model_creation()

    #X_train, y_train = DSC.create_data_set(DATASETDIR=DATASETDIR, LABEL=LABEL, IMAGE_SIZE=IMAGE_SIZE)
    #print('Train data set is created')

    #DLMC.ResNet50(input_shape=(IMAGE_SIZE, IMAGE_SIZE, IMAGE_DIMENSION), classes=CLASS, X_train=X_train, y_train=y_train,
    #              EPOCH=EPOCH, BATCH_SIZE=BATCH_SIZE, MODEL_OPTIMIZER=MODEL_OPTIMIZER, MODEL_LOSS=MODEL_LOSS,
    #              MODEL_METRICS=MODEL_METRICS, OUTPUT_LAYER_ACTIVATION=OUTPUT_LAYER_ACTIVATION)
    #print('Congratulations - Deep learning model is created ')

    print('Hurrayyyyyy Enjoy Life :)')
