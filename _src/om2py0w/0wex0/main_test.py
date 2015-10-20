# -*- coding: utf-8 -*-
import sys, os, glob
# print sys.getdefaultencoding()
reload(sys) # 必须 reload
sys.setdefaultencoding('utf-8')

# ===========调用脚本 外部数据 中英文
keywords = sys.argv[1:] # The list of command line arguments passed to a Python script
# 命令行中 除脚本名 以外的所有参数都保存在 keywords 中

print keywords 
print type(keywords) # 查看keyword 它是list 输入英文 print 英文

for words in keywords:
    # words = unicode(words, "ascii")
    # print words
    # print type(words)
    print words,

current_dir = os.getcwd()
print type(current_dir)
os.chdir(current_dir)

for file in glob.glob("*.txt"):
    print(file)
    file_content = open(file, "r")
    print file_content.read()

print """Congratulations: You have invoked the script main.py

-- I love coding in Python!
-- Do you love it?

Have fun in Python Star Trek!""" # 

# name = raw_input("请输入日志名: ".encode(sys.stdin.encoding)) + '.txt' # succeed
name = raw_input("请输入日志名: ".encode(sys.stdout.encoding)) + '.txt' # succeed
# name = raw_input("请输入日志名: ".decode('utf-8')) + ".txt"
# name = raw_input("Glad to write today's diary"
# "\n Please give the name first:") + '.txt' 
# 以上 提示中文 是乱码 pshell 会出现乱码 cat 我的日志.txt
# 以上 这输入中文名 也是乱码 
# 待解决 第二日 reboot之后 就自然解决了 amazing
# win 的 reboot 真是强

yes_list = ['yes', 'yep', 'ye', 'y', 'YES','YEP', 'YE', 'Y']
no_list = ['no', 'n', 'NO', 'N']

def ask_date(prompt, retries=3, friendly_warn='Please input yes or no'):
    ok = raw_input(prompt)
    if ok in yes_list:
        ur_date = raw_input("Please add date: ") # 这里可以调用模块 time
    if ok in no_list:
        ur_date = "\n"

    retries += -1
    if retries < 0:
        raise IOError('Refuselink user')
    print friendly_warn

    return ur_date

writer = open(name, "w") # if the textfile exist it'll be erased

done = False
textInput = ""

while (done == False):
    nextInput = raw_input("Please input ur words: ")
    if nextInput == "end": 
        inputDate = ask_date("Do you want add date, yes or no?")
        writer.write('\n' + inputDate)
        break
    else:
        textInput += nextInput
        print nextInput
        writer.write(nextInput + "\n") #  write into textfile.txt and start a new line

writer.close()

print ("Here is ur diary: " + textInput)

# ==================== 调用脚本 及其关键字 


# 交互
# ========== 调用 python脚本
# ========== 中文输入
# 在 pshell cmd line 中输入中文 如 我爱python
# 问题： 中文 我爱 这部分 输出的是 一种编码形式 解决之 
# 分析： 传递参数（中文字符）后 再次输出 可能没有解码还原为中文字符
# 方案： google search 原来 在最初运用了 utf-8 编码 输出的时候 没有 unicoding 
# keywords = unicode(keywords, "utf-8")
# 但是不能解码list error need string or buffer
# utf 解码错误
#     words = words.defcode("ascii").encode("utf-8")
# 在没有修改默认编码是 以上设置 也是错的
# 参考 http://www.kryptosx.info/archives/391.html
# ===========持续交互
# while 
# =========== 输出文件
# - 换行
# - 日期
# - 中文编码 
#    + 中文编码问题
#        + name = raw_input("请输入日志名: ") + '.txt' 在pshell中 乱码
#        + 分析
# UnicodeDecodeError: 'utf8' codec can't decode byte 0xb2 in position 0: invalid start byte
# 本身 sys.setdefaultencoding('utf-8') 是utf-8 编码的 在pshell中 raw_input("请输入日志名：") 中
# 双引号中的 请输入日志名 出现乱码 璇疯緭鍏ユ棩蹇楀悕
# =========== 回读文本
# - 自动将过往日志打印？
# http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python
# 	+ 如何找到日志文件
#	+ 如何打开
#	+ 如何读取
# 	+ 如何输出日志
#   + 中文OK么