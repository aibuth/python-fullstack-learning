# # 基本捕获语法
try:
    f = open("D:/abc.txt", "r", encoding="utf-8")
except:
    print("出现异常了,文件不存在,我将open的模式,改为w模式去打开")
    f = open("D:/abc.txt", "w", encoding="utf-8")

# 捕获所有异常
try:
    print(1 / 0)
except Exception as e:
    print(f"出现异常了,异常是{e}")
else:
    print("else,没有异常时执行")
finally:
    print("finally有没有异常都会执行")
    f.close()