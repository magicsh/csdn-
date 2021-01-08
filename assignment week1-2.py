import os


filesize = 0
def stat_filesize(target_dir):
    # 读取文件夹内容，当是文件时，累加文件大小，当是文件夹时，继续遍历
    content = os.listdir(target_dir)
    # 遍历目标文件夹内所有文件
    global filesize
    for f in content:
        f = os.path.join(target_dir, f)
        if os.path.isfile(f):
            filesize = filesize + os.path.getsize(f)  # 若当前为文件，则获取文件大小
        if os.path.isdir(f):
            stat_filesize(f)  # 继续遍历文件夹
    return filesize


total_size = stat_filesize('C:/Users/surface pro3/Desktop/PythonProj')
print('文件总大小为：',total_size)
