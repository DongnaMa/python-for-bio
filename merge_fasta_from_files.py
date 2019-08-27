import os

#文件夹目录
path = "C:/Users/牛奶变咖啡/Desktop/tree_result/fa"
#得到文件夹下面的所有文件名称
files = os.listdir(path)
s = []
for file in files:
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        f = open(path+'/'+file)
        iter_f = iter(f) #创建迭代器
        a = ''
        for line in iter_f: #遍历文件，一行行遍历，读取文本
            a = a + line
        s.append(a) #每个文件的文本保存到list中

with open(path+'/'+'all.txt', 'w') as result_file:
    s = ''.join(s)
    result_file.write(s)