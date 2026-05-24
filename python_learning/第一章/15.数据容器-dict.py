# 字典 -- key不能重复(如果重复,后面的值会覆盖前面的值),key必须得是不可变类型(str,int,float,tuple)
# dict1 = {"王林":678,"李慕婉":677,"韩立":654,"徐立国":549}
# print(dict1)
# print(type(dict1))
#
# # key必须得是不可变类型(str,int,float,tuple),不能是list,set,dict
# dict2 = {}
# print(dict2)
# print(type(dict2))
#
# # 访问
# print(dict1["李慕婉"]) #获取
# dict1["李慕婉"] = 688  #修改
# print(dict1)
#
# dict1 = {"王林":678,"李慕婉":677,"韩立":654,"徐立国":549}
# print(dict1)
# # 添加 - key不存在就是添加
# dict1["林默"] = 550
# print(dict1)
#
# # 修改 - key存在就是修改
# dict1["林默"] = 650
# print(dict1)
#
# #查询
# print(dict1["林默"])        #根据key获取value
# print(dict1.get("林默"))    #根据key获取value
# print(dict1.keys())          #获取所有的key
# print(dict1.values())        #获取所有的value
# print(dict1.items())       #获取所有的键值对 key:value
#
# # 删除
# score = dict1.pop("林默")
# print(score)
# print(dict1)
#
# del dict1["韩立"]
# print(dict1)
#
# #遍历
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]}: {item[1]}")
#
# for k,v in dict1.items():
#     print(f"{k}: {v}")



shopping_cart = {}
menu = """
########### 购物车系统 ###########
#        1. 添加购物车           #
#        2. 修改购物车           #
#        3. 删除购物车           #
#        4. 查询购物车           #
#        5. 退出购物车           #
################################
"""
print("欢迎使用购物车管理系统 ~")

while True:
    # 1. 制作菜单
    print(menu)

    # 2. 执行的具体操作
    choice = input("请选择要执行的操作(1-5):")
    match choice:
        case "1":  # 添加购物车
            goods_name = input("请输入要添加的商品名称:")
            goods_price = input("请输入要添加的商品价格:")
            goods_num = input("请输入要添加的商品数量:")

            if goods_name in shopping_cart:
                print("该商品已存在,请重新添加!")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完成")

        case "2":  # 修改购物车
            goods_name = input("请输入要修改的商品名称:")
            if goods_name not in shopping_cart:
                print("该商品不存在,请重新选择修改!")
                continue
            goods_price = input("请输入要修改的商品价格:")
            goods_num = input("请输入要修改的商品数量:")
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改完成!")

        case "3":  # 删除购物车
            goods_name = input("请输入要删除的商品名称:")

            if goods_name not in shopping_cart:
                print("该商品不存在,请重新选择!")
            else:
                del shopping_cart[goods_name]
                print("商品删除成功!")

        case "4":  # 查询购物车
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称:{goods_name},商品价格:{goods_info["price"]},商品数量:{goods_info["num"]}")

        case "5":  # 退出购物车
            print("已退出购物车")
            break

        case _:  # 匹配其他所有情况
            print("错误操作,请重新输入!")

