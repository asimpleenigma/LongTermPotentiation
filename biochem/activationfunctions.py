# Benjamin Lloyd Cloer
# activationfunctions.py

from numpy import tanh
from numpy import e

__all__ = ['constant', 'linear', 'step', 'logistic', 'd_logistic', 'tanh', 'd_tanh', 'differentiate']

def constant(x):
    return True
def linear(x):
    return x
def step(x):
    return x > 0
def logistic(x):
    return 1/(1+e**(-x))
def d_logistic(x):
    return logistic(x)*(1-logistic(x))
def d_tanh(x):
    return 1-(tanh(x))**2
# tanh is already defined in numpy

def differentiate(f):
    if   f == linear:
        return constant
    elif f == logistic:
        return d_logistic
    elif f == tanh:
        return d_tanh
    else:
        raise TypeError("Activation function unsupported")
