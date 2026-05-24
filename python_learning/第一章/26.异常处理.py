try:
    print("===================================")
    # print(my_name)
    # print(1 / 0)
    # print("ABC"[10])
    print("ABC".hello)
    print("===================================")

except NameError as e:
    print("名字不存在,请检查变量或函数名,异常信息:",e)
except ZeroDivisionError as e:
    print("0不能做被除数,异常信息:",e)
except IndexError as e:
    print("索引错误,异常信息:",e)
except AttributeError as e:
    print("异常信息:",e)

# except Exception as e:   #捕获所有异常
#     print("异常信息:",e)

finally:   #无论程序是否正常运行,finally代码块中的代码都会运行
    print("资源释放~")