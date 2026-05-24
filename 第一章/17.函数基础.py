# 函数的参数与返回值
import math

# 函数1:计算圆的面积
def circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

print(f"圆的面积为:{circle_area(10):.2f}")

# 函数2:计算长方形的的面积
def rectangle_area(length,width):
    """
    根据长方形的长和宽,计算长方形的面积
    :param width: 宽
    :param length:长
    :return: 长方形的面积
    """
    area = width * length
    return area

# help(rectangle_area)
print(rectangle_area(20,10))

# 函数3:计算圆的面积,周长(如果返回值有多个,返回值之间用逗号分隔)   多个返回值会封装到元组中
def circle_area_len(radius):
    """
    根据圆的半径,计算圆的面积和周长
    :param radius: 圆的半径
    :return: 圆的面积,圆的周长
    """
    return round(math.pi * (radius ** 2), 2),round(2 * math.pi * radius, 2)

al = circle_area_len(10)
print(al)
print(type(al))

area,len = circle_area_len(10)
print(area)
print(len)