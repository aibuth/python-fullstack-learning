def fun1():
    print("fun1()开始执行")
    print(1 / 0)
    print("fun1()结束执行")

def fun2():
    print("fun2()开始执行")
    fun1()
    print("fun2()结束执行")

def main():
    try:
        fun2()
    except Exception as e:
        print(f"出现异常了,异常是{e}")

main()