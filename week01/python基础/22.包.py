# 1.导入模块
# import module02.my_fun
#
# module02.my_fun.log_separator1()
# module02.my_fun.log_separator2()

# from module02 import my_fun
#
# my_fun.log_separator1()
# my_fun.log_separator2()

# 注意:如果要通过 from ... import * 导入包下的所有模块,需要__init__.py 文件中添加 __all__=[]
# from module02 import *
#
# my_fun.log_separator1()
# my_fun.log_separator2()


# 2.导入模块中的功能
# 相对路径:从当前文件所在目录开始查找
# from module02.my_fun import log_separator1,log_separator2

# 绝对路径:从项目的根目录下开始查找
from 第二章.module02.my_fun import log_separator1,log_separator3

log_separator1()
log_separator3()





