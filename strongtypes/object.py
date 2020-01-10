import ast
from copy import deepcopy
from runtypes.observer import Observer
from runtypes.string import Str

class Object(object):
    _track_old = False
    _old = None
    _value = None
    def __init__(self, val, track=False):
        self.data = Observer()
        self.data.bind_to(self.value_changed)
        self._value = val
        self._track_old = track
    def __assign__(self, val):
        self._value = val
    def __repr__(self):
        return self._value
    def __get__(self, instance, owner):
        return instance._value
    def __set__(self, instance, value):
        try:
            if type(value) == type(instance._value):
                instance.set_value(value)
            else:
                raise TypeError("Type not same")
        except:
            print("Assignation error here \n")
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self.set_value(value)
    def set_value(self, value):
        if self._track_old:
            self._old = deepcopy(self._value)
        self._value = value
        for callback in self.data._observers:
            if self._track_old:
                print('Changing value from {0}:{1} to {2}:{3}'.format(type(self._old), self._old, type(self._value), self._value))    
            else:
                print('Changing value to {0}:{1}'.format(type(self._value), self._value))
            callback(self._value)
    def value_changed(self, value):
        # Your ops here
        print("Value Changed to {0}".format(value))

if __name__ == "__main__":
    
    o = Object("Test", True)
    print(o.value, o)
    o.value = "20"
    print(o.value, o)
    # # AttributeError: 'str' object has no attribute 'value'
    o = "20"
    print(o.value, o)

