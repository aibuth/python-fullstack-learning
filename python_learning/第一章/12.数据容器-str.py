# 字符串特点:不可变性(无法修改),有序性,可迭代性

# s = "   Hello-Python-Hello-World    "
# # find()查找指定字符串第一次出现的索引位置
# index = s.find("-")
# print(index)
#
# # count()统计字符串在指定字符串中出现的次数
# c = s.count("o")
# print(c)
#
# # upper()转为大写
# su = s.upper()
# print(su)
#
# # lower()转为小写
# sl = s.lower()
# print(sl)
#
# # split()将字符串按照指定字符串切割 - 列表
# slist = s.split("-")
# print(slist)
#
# # strip()去除字符串两端的空格
# s1 = s.strip()
# print(s1)
#
# # replace()代替
# s2 = s.replace("-","_")
# print(s2)
#
# # startswith() / endswith()判断字符串是否以指定的字符串开头 / 结尾
# print(s.startswith("   Hello"))
# print(s.endswith("World    "))
# print("----------------------------------------")
# print(s)

# # 方式二:in 运算符 ---> 判断字串是否在字符串中,存在返回True,否则返回False
# mail = input("请输入邮箱:")
# if mail.count("@") == 1 and "." in mail:
#     print(f"{mail}是合法的邮箱")
# else:
#     print(f"{mail}是非法的邮箱")

# #输入一个字符串,判断该字符串是否有回文(两边对称)
# # 黄山落叶松叶落山黄
# # 上海自来水来自海上
# s = input("请输入一个字符串:")
# if s == s[::-1]:
#     print(f"{s}是回文")
# else:
#     print(f"{s}不是回文")

# 将用户输入的10个字符串,反转后全部转换为大写,然后记录在列表,最后将列表内容,遍历输出出来
result_list = []
for i in range(10):
    s = input(f"请输入第{i + 1}个字符串:")
    process = s[::-1].upper()
    result_list.append(process)
for item in result_list:
    print(item)