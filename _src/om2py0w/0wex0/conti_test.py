# -*- coding: utf-8 -*-
import sys
from time import localtime, strftime

reload(sys) # 必须 reload
sys.setdefaultencoding('utf-8')

script_statement = """ # 脚本说明：

    1.这是每日日志书写脚本
    2.请按照提示进行 日志书写
    
    祝您书写愉快！
    """

print(script_statement.encode(sys.stdout.encoding))

diary_name = raw_input("请输入日志名: ".encode(sys.stdout.encoding)) + '.txt'

yes_list = ['yes', 'yep', 'ye', 'y', 'YES','YEP', 'YE', 'Y']
no_list = ['no', 'n', 'NO', 'N']

def ask_date(prompt):
    ok = raw_input(prompt)
    if ok in yes_list:
        ur_date = strftime("%Y-%m-%d %H:%M:%S", localtime()) # 这里可以调用模块 time 参考
    if ok in no_list:
        ur_date = "\n"
    return ur_date

writer = open(diary_name, "w") # if the textfile exist it'll be erased

done = False
textInput = ""

while (done == False):
    nextInput = raw_input("Please input ur words: ") + "\n"
    if nextInput == "end" + "\n":  # must add "\n"
        inputDate = ask_date("Do you want add date, yes or no?")
        writer.write('\n' + inputDate)
        break
    else:
        textInput += nextInput
        print nextInput
        writer.write(nextInput) #  write into textfile.txt and start a new line

writer.close()

print ("Here is ur diary: " + textInput)