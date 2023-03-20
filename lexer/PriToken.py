#  输出
import math
import re
import TokenTable


class Lexer:
    def __init__(self):
        self.TOKEN = TokenTable.TOKEN

    def getToken(self, sentence):
        self.output_list = []
        if sentence:
            tokens = sentence.split()
            for token in tokens:
                try:
                    self.output_token(token)  
                except:
                    self.argument_lexer(token)
            self.output_token(';')

    def argument_lexer(self, argument):
        i = 0
        length = len(argument)
        while i < length:
            temp = ''
            if argument[i] in ['P', 'S', 'C', 'L', 'E', 'T', '*']:
                if argument[i] == '*':
                    i += 1
                    if i >= length:
                        self.output_token(argument[i])
                        break
                    elif argument[i] == '*':
                        self.output_token('**')
                    else:
                        i -= 1
                        self.output_token(argument[i])
                else:
                    temp = re.findall(r"[A-Z]+", argument[i:])[0]
                    self.output_token(temp)
                    i += len(temp)-1
                    if i >= length:
                        break
            elif argument[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                if argument[i] == '.':
                    i += 1
                    temp = re.findall(r"\d+", argument[i:])[0]
                    i += len(temp)-1
                    temp = '0.' + temp
                    self.output_token(temp, False)
                else:
                    temp = re.findall(r"\d+\.?\d*", argument[i:])[0]
                    i += len(temp)-1
                    self.output_token(temp, False)
                if i >= length:
                    break
            else:
                self.output_token(argument[i])
            i += 1

    # 输出函数
    def output_token(self, token, NotNumber=True):
        if NotNumber:
            print([token, self.TOKEN[token]])
        else:
            tempdic = {token: {'TYPE': 'NUMBER',
                               'VALUE': float(token), 'FUNCTION': None}}
            print([token, tempdic[token]])