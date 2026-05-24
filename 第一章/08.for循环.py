# # 计算100-500之间所有3的倍数的数字之和
# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
#     i += 1
# print(total)

# *  *  *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *  *
#
# m = int(input("请输入长方形的长度:"))
# n = int(input("请输入长方形的宽度:"))
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")
#     print()

# 嵌套循环案例:打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i +1):
#         print(f"{j} x {i} = {i * j}",end = "\t")
#     print()

# 等腰直角三角形
# m = int(input("请输入直角边的边长:"))
# for i in range(m):
#     for j in range(i +1):
#         print("*",end=" ")
#     print()


# 根据输入的数字,打印对印的数字金字塔
# n = int(input("请输入金字塔的行数:"))
# for i in range(1,n+1):
#     for j in range(1,i + 1):
#         print(j,end="\t")
#     print()


# 打印国际象棋棋盘
size = 8
for i in range(size):
    for j in range(size):
        if i % 2 == j % 2:
            print("■",end = "\t")
        else:
            print("□",end = "\t")
    print()


