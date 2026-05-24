# # 元组特点:可以重复,有序,不可修改
# # 定义
# t1 = (80,95,78,50,76,80,85,20)
# print(t1)
# print(type(t1))
#
# # 索引访问
# print(t1[0])
# print(t1[-1])
#
# # 切片
# print(t1[0:5:1])
#
# # count()统计元素个数
# print(t1.count("80"))
#
# # index() 获取元素的索引(第一个元素的位置)
# print(t1.index(50))
#
# # 注意点: 如果定义单元素的元组,单个元素之后需要加上都逗号,如(100,)
# t2 = ()
# print(t2)
# print(type(t2))

# 元组的组包与解包
# # 组包
# t1 = (5,7,9,10,2,23,12)
# t2 = 5,7,9,10,2,23,12
# print(t1)
# print(t2)
#
# # 解包
# # 基础解包(变量数量与容器的元素个数一致)
# a,b,c,d,e,f,g = t1
# print(a,b,c,d,e,f,g)
#
# # * 扩展解包(* 收集剩余的所有元素,封装列表list中)
# first,second,*other,last = t1
# print(first,second)
# print(other)
# print(last)
#
# *other,last2,last1 = t1
# print(other)
# print(last2)
# print(last1)

# #案例1:现有两个变量,a = 10,b = 20,将这两个变量值交换,输出
# a = 10
# b = 20
# a,b = b,a
# print(a,b)
#
# # 案例二:现有三个变量,分别为:a = 100,b = 200,c = 300,现需将这三个值进行交换,将abc的值赋值给cab,输出到控制台
# a = 100
# b = 200
# c = 300
# c,a,b = a,b,c
# print(a,b,c)

students = (
("S001", "王林",85,92,78),
("S002", "李沐婉",92,88,95),
("S003", "十三",78,85,82),
("S004","曾牛",88,79,91),
("S005","周轶",95,96,89),
("S006","王卓",76,82,77)
)
# 1.计算每个学生的总分,各科平均分,然后一并输出出来 --->{avg:.1f} --->保留一位小数
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
# 方式一:
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]}\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{avg:.1f}")


#方式二:元组解包
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id}\t{name} \t {chinese} \t {math} \t {english} \t {total} \t {avg:.1f}")
print()

# 2.统计各科成绩的最低分,最高分,平均分,并输出
chinese_score = [s[2] for s in students]
math_score = [s[3] for s in students]
english_score = [s[4] for s in students]
print(f"语文最低分:{min(chinese_score)},最高分:{max(chinese_score)},平均分:{sum(chinese_score) / len(chinese_score)}")
print(f"数学最低分:{min(math_score)},最高分:{max(math_score)},平均分:{sum(math_score) / len(math_score)}")
print(f"英语最低分:{min(english_score)},最高分:{max(english_score)},平均分:{sum(english_score) / len(english_score)}")
print()


# 3.查找成绩优秀(平均分>90)的学生,并输出
print("成绩优秀同学名单如下:")
# 方式一:
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     if avg > 90:
#         print(f"学号:{s[0]},姓名:{s[1]},平均分:{avg:.1f}")

# 方式二:元组解包
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"学号:{id},姓名:{name},平均分:{avg:.1f}")
