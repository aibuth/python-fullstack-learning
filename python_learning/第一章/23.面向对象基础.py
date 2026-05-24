# 定义类
# class Car:
#     # __init__ 方法是初始化的方法,会在对象创建时自动调用,可以在该方法中为对象设置对应的属性
#     # self: 是第一个参数, 表示当前所创建出来的实例对象
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#
# # 创建对象
# c1 = Car("red","BWM","X7",800000)
# print(c1.__dict__)
#
# c2 = Car("white","奔驰","E300",450000)
# print(c2.__dict__)



# 定义类:实例方法
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#
#     def running(self):
#         print(f"{self.brand} {self.name} 正在全速行驶中....")
#
#     def total_price(self,discount,rate):
#         """
#         计算提车的总费用,包含两个部分: 车的价格,税费
#         :param discount:折扣
#         :param rate:税率
#         :return:提车的总费用
#         """
#         total_price = self.price * discount + rate * self.price
#         return total_price
#
# #     测试
# c1 = Car("red","BWM","X7",800000)
#
# #     调用对象中的方法
# c1.running()
# total = c1.total_price(0.9,0.1)
# print(f"提车的总费用为:{total}元")



# 定义类: 魔法方法
# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#
#     def running(self):
#         print(f"{self.brand} {self.name} 正在全速行驶中....")
#
#     def total_price(self,discount,rate):
#         total_price = self.price * discount + rate * self.price
#         return total_price
#
#     def __str__(self):
#         return f"{self.color} {self.brand} {self.name} {self.price}"
#
#     def __eq__(self,other):
#         return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
#
#     def __lt__(self,other):
#         return self.price < other.price
#
# c1 = Car("white","BYD","汉",180000)
# print(c1)
#
# c2 = Car("white","BYD","汉",180000)
# print(c2)
#
# print(c1 == c2)
# print(c1 < c2)



# ---------------------实例属性与类属性---------------------
class Car:
    # 类属性
    wheel = 4
    tax_rare = 0.1

    def __init__(self,c_color,c_brand,c_name,c_price):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price

    def running(self):
        print(f"{self.brand} {self.name} 正在全速行驶中....")

    def total_price(self,discount,rate):
        total_price = self.price * discount + rate * self.price
        return total_price

c1 = Car("white","BYD","汉",180000)
print(c1.name)
print(c1.wheel)
print(Car.wheel)









