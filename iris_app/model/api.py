from keras.models import load_model
import numpy as np

def create_model():
    pass


def compile_model():
    pass


def train_model():
    pass


def test_model():
    pass


def use_model():
#     Returns a function
    def f(x1, x2, x3, x4):
        model = load_model('model/model.h5')
        x = np.array([x1, x2, x3, x4]).reshape(1, 4)
        y = model.predict(x)
        prob = np.amax(y) # the probability
        y = np.argmax(y)
        if y == 0:
            return 'Iris-setosa (with {:.1%} probability)'.format(prob)
        elif y == 1:
            return 'Iris-versicolor (with {:.1%} probability)'.format(prob)
        elif y == 2:
            return 'Iris-virginica (with {:.1%} probability)'.format(prob)
        else:
            return 'Unknown'
    return f



def plot_model():
    pass
