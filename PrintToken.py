import os
from scanner import PriScan

if __name__ == "__main__":
    # print("输入\t类型\t\t\t值\t\t函数")
    path = os.getcwd()
    PriScan.Scanner(path+r'\test.txt').analyze()