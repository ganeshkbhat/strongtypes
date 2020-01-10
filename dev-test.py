from runtypes.observer import *
from runtypes.object import *
from runtypes.string import *
import ast
from ast2json import ast2json

def String(str: object) -> None:
    def __setattr__(self, attr, value):
        # our hook to do something
        print(f'set value of {attr} to {value}')
        # actually set the attribute the normal way after
        super().__setattr__(attr, value)
    def __call__(self, val):
        print("Value is assigned")
        self._value = val
    return str
    
class Name:
    pass

__builtins__.__dict__.update(**dict(object=Object, str=str))

o = Object("Test", True)
# print(o.value, o)
o.value = "20"
# print(o.value, o)
# # AttributeError: 'str' object has no attribute 'value'
o = str(30)
# print(o)
# print(o, __builtins__.__dict__)

f = open(file="./dev-test.py", mode="r")
code = f.read()
tree = ast.parse(code)
lines = [None] + code.splitlines()  # None at [0] so we can index lines from 1
test_namespace = {}

# print(ast2json(tree))
from json2xml import json2xml, readfromstring
print(json2xml.Json2xml(readfromstring(ast2json(tree))).to_xml())
# for idx, node in enumerate(tree.body):
#     wrapper = ast.Module(body=[node])
#     # print(ast.dump(wrapper))
#     if isinstance(node, ast.FunctionDef):
#         d = node.__dict__
#         print("FunctionName: ", node.name, ', Returns: ',d.get('returns').value)
#         [print('arg: ',i.arg, ', Annotation: ', i.annotation.id) for i in d.get('args').args]
#     if isinstance(node, ast.ClassDef):
#         d = node.__dict__
#         print(node.name)
