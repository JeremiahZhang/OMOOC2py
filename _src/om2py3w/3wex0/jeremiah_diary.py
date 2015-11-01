# -*- coding: utf-8 -*-
import sys, os, glob
from time import localtime, strftime

reload(sys)                       # 必须 reload
sys.setdefaultencoding('utf-8')

def main():

    read_diary()

    write_diary()

def welcome_statement():
    """ # Dear, welcome abord in Diary Ship

    1. Please input your words as following prompt
    2. Wanna Leave? Please input the word "end" alone
    3. Thanks, Hope you have fun in writing. > <

    Let's Start. GO
    """

def read_diary():

    current_dir = os.getcwd() # 打印之前日志
    os.chdir(current_dir)

    filename_plus_content =""

    for file in glob.glob("*.log"):
        # print(file) # this is the file name
        file_content = open(file, "r")
        diary = file_content.read() + "\n"
        filename_plus_content = filename_plus_content + file + "--->:" +diary
        print filename_plus_content
    return filename_plus_content

def write_diary():
    done = False
    textInput = ""

    diary_name = raw_input("请输入日志名: ".encode(sys.stdout.encoding)) + ".log"
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
    yes_list = ['yes', 'yep', 'ye', 'y', 'YES','YEP', 'YE', 'Y']
    no_list = ['no', 'n', 'NO', 'N']

    ok = raw_input(prompt)
    if ok in yes_list:
        your_datetime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if ok in no_list:
        your_datetime = "\n"

    return your_datetime

if __name__ == '__main__':
    main()