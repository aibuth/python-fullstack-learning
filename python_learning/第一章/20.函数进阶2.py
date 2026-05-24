# 函数的参数类型
# # 加
# def add(x,y):
#     return x+y
# # 减
# def sub(x,y):
#     return x-y
# # 乘
# def mul(x,y):
#     return x*y
# # 除
# def div(x,y):
#     return x/y
#
# # 计算
# def calc(x,y,oper):
#     return oper(x,y)
#
# print(calc(10,20,add))
# print(calc(10,20,sub))
# print(calc(10,20,mul))


# 匿名函数
# def out_line():
#     print("------------------------------")

# out_line = lambda : print("------------------------------")
# out_line()
#
# # 需求二:计算两数之和
# add = lambda x,y : x + y
# print(add(12,20))
#
#
# # 需求三:完成如下列表的排序操作,按照每个元素的字符个数,从小到大排序
# data_list = ["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
# print(data_list)
#
# data_list.sort(key = lambda item : len(item),reverse = False)#匿名函数典型的应用场景
# print(data_list)



# 案例一:计算n的阶乘
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# result = factorial(10)
# print(result)



"""
案例2：定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
具体规则如下:
1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""
def calc_order_cost(*args,coupon = 0,score = 0,charges = 0):
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

#     优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

#     积分
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

#     运费
    total_cost -= charges
    return total_cost

# 测试
total = calc_order_cost(("手机",5999,5),("电脑",12999,3),("鼠标",156,15),("键盘",462,10),coupon = 100,score = 10000,charges = 500)
print(total)












