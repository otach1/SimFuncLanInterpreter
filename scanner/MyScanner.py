import re
from lexer import MyLexer


class Scanner():
    def __init__(self, path):
        # 文件位置
        self.path = path
        # 缓冲区
        self.text = ""
        with open(self.path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # 将文件中注释去掉
                self.text = self.text + \
                    line.split("//")[0].split("--")[0].split("\n")[0]
        self.text = self.text.upper().strip()
        self.lexer = MyLexer.Lexer()
        self.output_lists = []

    def analyze(self):
        sentences = re.split("(;)", self.text)
        # 识别
        # E->E;|ε
        state = True
        for sentence in sentences:
            if state and sentence != ";":
                state = False
                self.lexer.getToken(sentence)
                self.output_lists.extend(self.lexer.output_list)
            elif sentence == ";":
                state = True
            else:
                raise SyntaxError()
        if state:
            raise SyntaxError()
        return self.output_lists
