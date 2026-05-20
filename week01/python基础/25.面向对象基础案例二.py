"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：

1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
5. 退出购物车
"""

# 商品类
class Goods:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称：{self.name}，商品价格：{self.price}，商品数量：{self.num}"

    def modify_goods(self,price=None,num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num


# 购物车类
class ShoppingCart:
    def __init__(self):
        self.ShoppingCart_list = []

    #    添加购物车
    def add_goods(self):
        name = input("请输入要添加的购物车商品名称:")

        for g in self.ShoppingCart_list:
            if g.name == name:
                print("购物车商品已存在,添加失败!")
                return

        price = float(input("请输入要添加的购物车商品的价格:"))
        num = int(input("请输入要添加的购物车商品的数量:"))

        gds = Goods(name,price,num)
        self.ShoppingCart_list.append(gds)
        print("购物车商品添加成功")


    #     修改购物车
    def update_goods(self):
        name = input("请输入要修改的购物车商品名称:")

        for g in self.ShoppingCart_list:

            if g.name == name:
                print(f"购物车商品当前信息:{g}")

                price = float(input("请输入要修改的购物车商品的价格:"))
                num = int(input("请输入要修改的购物车商品的数量:"))

                g.modify_goods(price,num)
                print("购物车商品修改成功")
                return
        print("未找到该购物车商品,修改失败")


    #     删除购物车
    def del_goods(self):
        name = input("请输入要删除的购物车商品名称:")

        for g in self.ShoppingCart_list:
            if g.name == name:
                self.ShoppingCart_list.remove(g)
                print("该购物车商品删除成功")
                return

        print("未找到该购物车商品,删除失败")


    #     查询购物车商品
    def query_goods(self):
        name = input("请输入要查询的购物车商品名称:")

        for g in self.ShoppingCart_list:
            if g.name == name:
                print(f"购物车商品信息为: {g}")
                return

        print("未找到该购物车商品,查询失败")


    #     查询所有购物车商品
    def list_goods(self):
        for g in self.ShoppingCart_list:
            print(g)


    #     运行系统
    def run(self):
        print("欢迎使用购物车管理系统!")

        while True:
            print()
            print("#########################################################################################################")
            print("# 1. 添加购物车商品   2. 修改购物车商品   3. 删除购物车商品   4. 查询指定购物车商品   5. 查询所有购物车商品   6. 退出系统 #")
            print("#########################################################################################################")
            print()

            choice = input("请输入要执行的操作(1 - 6):")

            try:
                match choice:
                    case "1":
                        self.add_goods()
                    case "2":
                        self.update_goods()
                    case "3":
                        self.del_goods()
                    case "4":
                        self.query_goods()
                    case "5":
                        self.list_goods()
                    case "6":
                        print("已退出购物车商品管理系统~")
                        break
                    case _:
                        print("输入操作有误,请输入正确的数字!")
            except Exception as e:
                print("输入有误,请检查后重新输入,异常信息为:",e)

gds_shopping_cart = ShoppingCart()
gds_shopping_cart.run()
