import os
import MyInterpreter

if __name__ == '__main__':
    path = os.getcwd()
    MyInterpreter.Interpreter(path+r'\test.txt').create()
