# -*- coding: utf-8 -*-
import sys, os, glob
from time import localtime, strftime

reload(sys)                       # 必须 reload
sys.setdefaultencoding('utf-8')

yes_list = ['yes', 'yep', 'ye', 'y', 'YES','YEP', 'YE', 'Y']
no_list = ['no', 'n', 'NO', 'N']

def main():
    keywords = sys.argv[1:] # 调用外部数据
    for words in keywords:
        print words,
    print "\n"
    
    read_diary()
    
    script_statement = """ # 脚本说明：

    1.这是每日日志书写脚本
    2.首先打印的是脚本所在文件夹所有日志(txt格式)名称及内容
    3.请按照提示进行 日志书写
    4.想要结束日志写作？最后一行请单独输入：end
    
    祝您书写愉快！
    """
    
    print(script_statement.encode(sys.stdout.encoding) + "\n")
    
    write_diary()

def read_diary():
    current_dir = os.getcwd() # 打印之前日志
    os.chdir(current_dir)

    for file in glob.glob("*.txt"):
        print(file)
        file_content = open(file, "r")
        print file_content.read() + "\n"

def write_diary():
    done = False
    textInput = ""

    diary_name = raw_input("请输入日志名: ".encode(sys.stdout.encoding)) + ".txt"
    diary_writer = open(diary_name, "w")

    while (done==False):
        nextInput = raw_input("Please input your diary words:  ")
        if nextInput == "end":
            inputDate = ask_date("Wanna add diary date time? yes or no! ")
            diary_writer.write("\n" + inputDate)
            break
        else:
            textInput += nextInput + "\n"
            diary_writer.write(nextInput + "\n")

    diary_writer.close()
    print ("Here is your " + inputDate +" diary: " + textInput)

def ask_date(prompt):  # 是否添加时间
    ok = raw_input(prompt)
    if ok in yes_list:
        your_datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if ok in no_list:
        your_datetime = "\n"
    
    return your_datetime

if __name__ == '__main__':
    main()