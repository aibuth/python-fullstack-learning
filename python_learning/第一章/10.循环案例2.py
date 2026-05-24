# import random
# random_num = random.randint(1,100)
# while True:
#     num = int(input("请输入一个数字:"))
#     if num > random_num:
#         print("您输入的数字太大了!")
#     elif num < random_num:
#         print("您输入的数字太小了!")
#     else:
#         print("恭喜您,猜对了!")
#         break
# print(f"随机生成的数字是{random_num}")

# 将1-1000之间所有的5的倍数的数字加起来
total = 0
for i in range(1,1001):
    if i % 5 == 0:
        total += i
print(f"和为{total}")