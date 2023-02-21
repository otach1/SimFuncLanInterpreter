import os
from parser import ParserTree

if __name__ == '__main__':
    path = os.getcwd()
    ParserTree.Parser(path+r'\test.txt').analyze()
