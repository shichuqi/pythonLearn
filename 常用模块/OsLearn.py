import os

mydir = os.getcwd()
print(mydir)
print('*'*20)

# os.chdir('/Users')
# print(os.getcwd())

print(os.listdir(mydir))
print('*'*20)

# os.makedirs('tset')
# print(os.listdir(mydir))

# system执行系统命令
result = os.system('ls')
print(result)
print('*'*20)

# 获得系统变量
print(os.getenv('PATH'))
print('*'*20)

print(os.pardir)
print(os.curdir)
print(os.linesep)
print(os.sep)

print('*'*20)

print('{0}Users{0}'.format(os.sep))
print('*'*20)

#Linux系统名称叫 posix
print(os.name)
print('*'*20)


# 相对路径转绝对路径
print(os.path.abspath('.'))
# 或者
import os.path as op
print(op.abspath('.'))
print('*'*20)

# 获取路径中文件名部分
print(op.basename(op.abspath('.')))
print('*'*20)

# join将多个路径拼成一个路径  跟多操作看完整教程项目

print('*'*20)

# isdir() 是否是目录  op.exists() 是否存在


# shuril模块

# copy 拷贝 shutil(来源路径，目标路径)  返回值：目标路径   拷贝同时可以重命名
import  shutil
# rst = shutil.copy('./01.py','./01_copy1.py')
# print(rst)

print('*'*20)

# copyfile()讲一个文件中的内容拷贝到另一个文件中
# move 移动文件

# 归档和压缩

# make_archive() 归档，大小不变
# rst = shutil.make_archive('./归档实验','zip','../常用模块')

# zip-压缩  模块名 zipfile
import zipfile
zf = zipfile.ZipFile('./归档实验.zip')
print(zf)

# 解压缩 extractall()





































