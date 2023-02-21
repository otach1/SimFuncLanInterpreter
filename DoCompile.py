import os
import MyCompile

if __name__ == '__main__':
    path = os.getcwd()
    MyCompile.Compile(path+r'\test.txt', path+r'\output.py').create()
