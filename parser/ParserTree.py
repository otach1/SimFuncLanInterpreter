# 打印语法树
import ast
import astunparse
from scanner import MyScanner


class Parser:
    def __init__(self, path):
        self.scanner = m=MyScanner.Scanner(path)
        self.dataflow = self.scanner.analyze()
        self.i = 0 
        self.length = len(self.dataflow)  

    def analyze(self):
        print('enter in program')
        self.i = 0
        while(self.i < self.length):
            if self.dataflow[self.i][1]['TYPE'] == 'KEYWORD':
                self.output(self.dataflow[self.i][0])

    def output(self, string):
        print('enter in '+string.lower()+'_statement')
        print('matchtoken '+string.upper())
        self.i += 1
        if string == 'ORIGIN' or string == 'SCALE':
            self.ORIGIN_or_SCALE()
        elif string == 'ROT':
            self.ROT()
        elif string == 'FOR':
            self.FOR()
        else:
            raise SyntaxError()
        print('exit from '+string.lower()+'_statement')

    def ORIGIN_or_SCALE(self):
        self.matchstring('IS')
        templist = self.matchparameter()
        self.outputTree(templist[0])
        self.outputTree(templist[1])

    def ROT(self):
        self.matchstring('IS')
        self.outputTree(self.matchexpression())

    def FOR(self):
        self.matchstring('T')
        self.matchstring('FROM')
        self.outputTree(self.matchexpression())
        self.matchstring('TO')
        self.outputTree(self.matchexpression())
        self.matchstring('STEP')
        self.outputTree(self.matchexpression())
        self.matchstring('DRAW')
        templist = self.matchparameter()
        self.outputTree(templist[0])
        self.outputTree(templist[1])

    def matchstring(self, string):
        if self.dataflow[self.i][0] == string:
            print('matchtoken '+string)
            self.i += 1
        else:
            raise SyntaxError()

    def matchparameter(self):
        temp = self.matchexpression()  
        # 转换为列表[E,E]
        if temp[0] == '(' and temp[-1] == ')':
            temp = temp[1:-1].split(',')
        else:
            raise SyntaxError()
        return temp

    def matchexpression(self):
        temp = ''  
        while(self.dataflow[self.i][0] != ';' and self.i < self.length and self.dataflow[self.i][1]['TYPE'] != 'KEYWORD'):
            if self.dataflow[self.i][1]['TYPE'] == 'FUNC':
                temp += self.dataflow[self.i][1]['FUNCTION']
            elif self.dataflow[self.i][1]['TYPE'] == 'CONST_ID':
                temp += str(self.dataflow[self.i][1]['VALUE'])
            else:
                temp += self.dataflow[self.i][0]
            self.i += 1
        if self.dataflow[self.i][0] == ';':
            self.i += 1  
        return temp

    # 输出语法树
    def outputTree(self, string):
        print('enter in expression')
        print(astunparse.dump(ast.parse(string, filename='<unknown>')))
        print('exit from expression')
