import ast
from copy import deepcopy

class Observer(object):
    def __init__(self):
        self._observers = []
    def bind_to(self, callback):
        print('Bound Oberver')
        self._observers.append(callback)