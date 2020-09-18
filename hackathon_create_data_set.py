########################################################################################################################
# Name of file: hackathon_create_data_set.py
# Description: This file creates train and test data set
# Revision: 1.0
# Last Update:
# Authors:
########################################################################################################################

#Importing python moddules
import os
import cv2
import math
import random
import numpy as np
from keras.utils import to_categorical

#Global Variables
DATASETDIR = '<Your local path>'  #Parent directory of videos
IMAGE_SIZE = 256  #Image Size
LABEL = [0, 1, 2, 3, 4, 5, 6, 7, 8]

class data_set_creation:

    #Function Description: Create train and test data set
    #Function Input: Parent directory of images
    #Function Output: Training data set - X_train and y_train
    def create_data_set(self, DATASETDIR, LABEL, IMAGE_SIZE):

    #Local variable definition
        X_train = []
        y_train = []
        X_temp = []
        y_temp = []
        tmp_X = []
        i = 0
        m = 0

        for dir in os.listdir(DATASETDIR):
            path = DATASETDIR + '/' + dir + '/'
            for files in os.listdir(path):
                i = i + 1
                img_array = cv2.imread(os.path.join(path, files))  #Read image
                new_array = cv2.resize(img_array, (IMAGE_SIZE, IMAGE_SIZE))  #resize the image to 256x256
                X_temp.append([new_array, LABEL[m]])
            m = m + 1

        #Shuffling the data for more randomness
        random.shuffle(X_temp)

        #Seperating data and label
        for i, j in X_temp:
            tmp_X.append(i)
            y_temp.append(j)

        #Converting list to numpy
        X = np.array(tmp_X).reshape(-1, IMAGE_SIZE, IMAGE_SIZE, 3)
        Y = np.array(y_temp).reshape(-1, 1)

        #Normalize image vectors
        X_train = X/255

        #Converting the label to binary values
        y_train = to_categorical(Y)

        #Debug messages
        print('shape of X is ', X.shape)
        #print ('X_train is ', X_train[0])
        #print ('X_train length is ', len(X_train))
        #print ('y_train is', y_train[0])
        #print ('y_train length is ', len(y_train))
        #print ('y_train is ', y_train[137])
        #print ('y_train is ', y_train[2238])
        #print ('X is', X)
        #print ('length of X is ', len(X[0]))
        return X_train, y_train


if __name__ == "__main__":
    #print('Creating class handles for classes')
    #DSC = data_set_creation()
    #print('Use the below call of SCDF.main only if you want run this file independently')
    #X_train, y_train = DSC.create_data_set(DATASETDIR=DATASETDIR, LABEL=LABEL, IMAGE_SIZE=IMAGE_SIZE)

    print('Hurrayyyyyy Enjoy Life :)')
