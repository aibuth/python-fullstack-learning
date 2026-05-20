# 对形参进行类型注解
def add(a: int,b: int):
    return a+b
print(add(1,2))


# 对返回值进行类型注解
def func(data: list) -> list:
    return data
print(func([1,2,3]))
