import os
import os.path

with open('out.tab', 'w') as result_file:
    # 文件夹目录
    path = "C:/Users/牛奶变咖啡/Desktop/tree_result/fa"
    # 得到文件夹下面的所有文件名称
    files = os.listdir(path)

    for file in files:
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            if os.path.splitext(file)[1] == '.out':
                f = open(path + '/' + file)
                for line in f:
                    line = line.strip()
                    result_file.write(line + "\n")
