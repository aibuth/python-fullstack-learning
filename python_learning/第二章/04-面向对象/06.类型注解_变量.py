"""
var_1: int =  123
var_2: str = "123"
var_3: bool = True

class Student:
    pass
stu: Student = Student()

my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"a": 1, "b": 2, "c": 3}

my_list2: list[int] = [1, 2, 3]
my_tuple2: tuple[int,str,bool] = (1, "aaa", True)
my_dict2: dict[str,int] = {"a": 1, "b": 2, "c": 3}
"""
import random
import json
# 在注释中进行类型注解
var_1 = random.randint(1, 100)  #type: int
var_2 = json.loads('{"a": 1, "b": 2, "c": 3}')    #type: dict
print(type(var_2))
def func():
    return 10
var_3 = func()   #type: int
