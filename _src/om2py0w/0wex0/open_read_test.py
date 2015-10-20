import os, glob

current_dir = os.getcwd()
print type(current_dir)
os.chdir(current_dir)

for file in glob.glob("*.txt"):
    print(file)
    file_content = open(file, "r")
    print file_content.read()