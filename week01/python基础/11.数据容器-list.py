# s = [11,22,33,44,55,66,77,"abc",True]
# print(type(s))
# print(s[0])
# print(s[-1])
# s[2] = 456
# print(s)
# del s[0]
# print(s)
# # 遍历
# for item in s:
#     print(item)

# 切片操作 s[开始索引:结束索引:步长]
# s = ["A","O","H","U","F","K","R","B"]
# print(s[0:5:1])
# print(type(s[0:5:1]))
#
# print(s[0:5])
# print(s[:5:])
# print(s[:5])


# 列表定义
# s = [56,90,88,65,90,100,209,72,145]
# print(s)
#
# # append(): 在列表尾部追加元素
# s.append(188)
# print(s)
#
# # insert():在指定索引前,插入元素
# s.insert(2,80)
# print(s)
#
# # remove():移除列表中第一个匹配到的元素
    # s.remove(90)
# print(s)
#
# # pop():删除列表中指定索引位置的元素并返回
# e = s.pop(1)
# print(e)
#
# e = s.pop()
# print(e)
# print(s)
#
# # sort():排序
# s.sort()
# print(s)
#
# # reverse():反转列表元素
# s.reverse()
# print(s)



# # 案例1:将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值,最大值,平均值
# num_list = []
# for i in range(10):
#     num = int(input(f"请输入第{i + 1}个数字:"))
#     num_list.append(num)
# print(num_list)
#
# num_list.sort()
# print(num_list)
#
# print(f"最大值为:{num_list[0]}")
# print(f"最小值为:{num_list[-1]}")
# print("平均值:",sum(num_list) / len(num_list))

# # 案例2:合并两个列表中的元素,并对合并后的结果进行去重处理
# num_list1 = [123,456,789,951,357,654,781,685,354,125,456]
# num_list2 = [654,852,963,147,741,369,258]
#
# num_list3 = num_list1 + num_list2
# print("合并后的原始列表为:",num_list3)
#
# new_list = []
# for num in num_list3:
#     if num not in new_list:
#         new_list.append(num)
# print("去除重复后的列表:",new_list)

# # 案例三:生成1-20的平方列表
# # 方式一:传统方式
# num_list = []
# for num in range(1,21):
#     num_list.append(num ** 2)
# print(num_list)
# # 方式二:列表推导式
# num_list2 = [i ** 2 for i in range(1,21)]
# print(num_list2)

# 案例四:从一个数字列表中提取所有偶数,并计算其平方,组成一个新的列表
num_list = [11,22,56,96,48,57,35,26,49,51,124,27,63,111,123,132]
num_list2 = [i ** 2 for i in num_list if i % 2 == 0]
print(num_list2)