import theano
from theano import tensor as T
import numpy as np

from util.load import mnist
from util.fig import plot_first_k_numbers

def floatX(X):
    return np.asarray(X, dtype=theano.config.floatX)

def init_weights(shape):
    '''Initialize model parameters'''
    return theano.shared(floatX(np.random.randn(*shape) * 0.01))

def model(X, w):
    '''Model in matrix format'''
    return T.nnet.softmax(T.dot(X, w))

# Loading data 
trX, teX, trY, teY = mnist(onehot=True)

X = T.fmatrix()
Y = T.fmatrix()

w = init_weights((784, 10))

# probability outputs and maxima predictions
py_x = model(X, w)
y_pred = T.argmax(py_x, axis=1)

# cost function to optimize
cost = T.mean(T.nnet.categorical_crossentropy(py_x, Y))
gradient = T.grad(cost=cost, wrt=w)
update = [[w, w - gradient * 0.05]]

train = theano.function(inputs=[X, Y], outputs=cost, updates=update, allow_input_downcast=True)
predict = theano.function(inputs=[X], outputs=y_pred, allow_input_downcast=True)

# Train on mini-batched of 128 examples
for i in range(3):
    for start, end in zip(range(0, len(trX), 128), range(128, len(trX), 128)):
        cost = train(trX[start:end], trY[start:end])
	
	plot_first_k_numbers(trX, 128)
    print i, np.mean(np.argmax(teY, axis=1) == predict(teX))

