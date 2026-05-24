# 计算1-100之间所有偶数的和
total = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1-100之间所有偶数的和为:{total}")