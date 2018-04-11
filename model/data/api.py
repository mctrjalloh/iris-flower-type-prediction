import pandas as pd
import numpy as np
import random

FILENAME = 'data/iris.data.txt'  # provide the name of the file to be saved


def create_data():
    # saves data into FILENAME
    pass


def read_data():
    # returns a numpy array representation of the data after reading FILENAME
    df = pd.read_csv(FILENAME, header=None)
    df.replace(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], [0, 1, 2], inplace=True)
    data =  np.array(df)
    data_list = list(data)
    random.shuffle(data_list)
    return np.array(data_list)

    
def preprocess_data(data):
    # returns a couple of numpy arrays representing (inputs, labels)
    inputs = np.array([data[i][:4] for i in range(len(data))])
    labels = np.array([data[i][-1] for i in range(len(data))]).astype(int)
    return (inputs, labels)

inputs, labels = preprocess_data(read_data())
SPLIT_RATIO = 0.8  # to be changed as necessary
SPLIT_SIZE = int(SPLIT_RATIO * len(inputs))


def training_data():
    # returns a tuple of (inputs, labels)
    global inputs, labels
    return inputs[:SPLIT_SIZE], labels[:SPLIT_SIZE]


def testing_data():
    # returns a tuple of (inputs, labels)
    global inputs, labels
    return inputs[-(len(inputs) - SPLIT_SIZE):], labels[-(len(inputs) - SPLIT_SIZE):]


def plot_data():
    pass
