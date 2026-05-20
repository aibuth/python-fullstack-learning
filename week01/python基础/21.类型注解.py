# 函数类型注解
# def circle_area_len(r: float) -> tuple[float, float]:
#     return round(3.14 * r ** 2, 1), round(2 * 3.14 * r, 1)
#
# al = circle_area_len(8.5)
# print(al)


def calc_order_cost(*args: tuple[str,float,int],coupon: int = 0,score: int = 0,charges: float = 0.0):
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
