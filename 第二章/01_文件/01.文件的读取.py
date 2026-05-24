# 打开文件
f = open("D:/测试.txt","r",encoding = "utf-8")

# 读取文件 - read()
# print(f"read方法读取的全部内容是:\n{f.read()}")

# 读取文件 - readLines()
# print(f"readLines方法读取的内容是:\n{f.read()}")#读取文件的全部行,封装到列表当中

# 读取文件 - readLine()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是:{line1}")
# print(f"第二行数据是:{line2}")
# print(f"第三行数据是:{line3}")

# for循环读取文件行
for line in f:
    print(line)

# 关闭文件
f.close()

# with open 语法操作文件
# with open("D:/测试.txt","r",encoding = "utf-8") as f:
#     print(f.read())



