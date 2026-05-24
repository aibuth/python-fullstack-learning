# 使用Union类型,必须先导包
from typing import Union
my_list: list[Union[int, str]] = [1, 2, "a","b"]

def func(data: list[Union[int,str]]) -> list[Union[int,str]]:
    return data