import math
import re
import TokenTable


class Lexer:
    def __init__(self):
        # 从文件中读取记号表
        self.TOKEN = TokenTable.TOKEN

    def getToken(self, sentence):
        self.output_list = []
        if sentence:
            tokens = sentence.split()
            for token in tokens:
                try:
                    # ORIGIN|SCALE|ROT|IS|FOR|FROM|TO|STEP|DRAW|ε (可直接识别)
                    self.output_token(token)
                except:
                    # 需要更高级的DFA中识别
                    self.argument_lexer(token)
            self.output_token(';')

    def argument_lexer(self, argument):
        i = 0  # 字符串长度
        length = len(argument)  # 字符串长度
        while i < length:
            # 临时字符串,即缓冲区
            temp = ''
            if argument[i] in ['P', 'S', 'C', 'L', 'E', 'T', '*']:

                # 识别"*"还是"**"
                # C
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
                    # PI|E|T|SIN|COS|TAN|LOG|EXP|SQRT
                    temp = re.findall(r"[A-Z]+", argument[i:])[0]
                    # 是否接受
                    self.output_token(temp)
                    i += len(temp) - 1
                    if i >= length:
                        break
                    
            elif argument[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                # 识别数字
                if argument[i] == '.':
                    # 识别开头为"."的数字
                    i += 1
                    temp = re.findall(r"\d+", argument[i:])[0]
                    i += len(temp) - 1
                    temp = '0.' + temp
                    self.output_token(temp, False)
                else:
                    # 识别一般数字
                    # [0-9]+.[0-9]*
                    temp = re.findall(r"\d+\.?\d*", argument[i:])[0]
                    i += len(temp) - 1
                    self.output_token(temp, False)
                if i >= length:
                    break

            else:
                # 识别其他字符
                self.output_token(argument[i])
            i += 1

    # 输出函数
    def output_token(self, token, NotNumber=True):
        if NotNumber:
            self.output_list.append([token, self.TOKEN[token]])
        else:
            tempdic = {token: {'TYPE': 'NUMBER',
                               'VALUE': float(token), 'FUNCTION': None}}
            self.output_list.append([token, tempdic[token]])
