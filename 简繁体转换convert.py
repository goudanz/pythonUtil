import zhconv
import sys
import os

# pip install zhconv

def convertToZhtw(inputTsPath, outTsPath):
    with open(inputTsPath,'r', encoding='UTF-8') as f:
        content = f.read()
        with open(outTsPath,'w',encoding='UTF-8') as f1:
            f1.write(zhconv.convert(content, 'zh-cn'))


for files in os.listdir('D:\java\python\convet'):
    
    oldfile = files
    newfile = os.path.splitext(oldfile)[0]

    convertToZhtw(oldfile, newfile + '_cn.json');

