import os

path = "C:/Users/牛奶变咖啡/Desktop/tree_result/fa"
files = os.listdir(path)
n = 0
for file in files:
    if not os.path.isdir(file):
        oldname = path + os.sep + files[n] #设置旧文件名（就是路径+文件名）,os.sep添加系统分隔符
        newname = path + os.sep + 'c' + str(n + 1) + '.fasta'  #设置新文件名
        os.rename(oldname, newname)  #用os模块中的rename方法对文件改名
        print(oldname, '======>', newname)
        n += 1


import os

path = "C:/Users/牛奶变咖啡/Desktop/tree_result/fa"
files = os.listdir(path)

for file in files:
    if not os.path.isdir(file):
        oldname = path + os.sep + file
        newname = path + os.sep + 'd' + file + '.fasta' 
        os.rename(oldname, newname)
        print(oldname, '======>', newname)


