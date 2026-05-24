# ------------------------------------ 函数 - 不定长参数(位置参数 *args --> 元组) -------------------------------------
# 需求:根据传入的这批数据,计算这批数据的最小值,最大值,平均值
# def calc_date(*args):
#     min_date = min(args)
#     max_date = max(args)
#     avg_date = sum(args) / len(args)
#     return min_date, max_date, round(avg_date,2)
#
# print(calc_date(2,7,9,10,45))
# print(calc_date(2,7,9,10,45,73,37,92,93,111,222))


# ------------------------------------ 函数 - 不定长参数(关键字参数 **kwargs --> 字典) -------------------------------------
# 需求:根据传入的这批数据,计算这批数据的最小值,最大值,平均值

def calc_date(*args,**kwargs):
    """
    根据传入的这批数据,计算这批数据的最小值,最大值,平均值
    :param args: 不定长位置参数
    :param kwargs:不定长关键字参数
    :return:最小值,最大值,平均值
    """
    min_date = min(args)
    max_date = max(args)
    avg_date = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_date = round(avg_date,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最小值:{min_date},最大值:{max_date},平均值:{avg_date}")

    return min_date, max_date, avg_date

print(calc_date(2,7,9,10,45,round = 3,print=True))
print(calc_date(2,7,9,10,45,73,37,92,93,111,222,round = 2,print=True))




