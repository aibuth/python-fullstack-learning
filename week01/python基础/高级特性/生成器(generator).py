"""
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L)
print(g)

print(next(g))
print(next(g))
print(next(g))

g = (x * x for x in range(10))
for x in g:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(10))
"""





# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
"""
核心逻辑
杨辉三角的每一行，首尾元素都是1，中间的元素等于上一行相邻两个元素之和。
生成器函数用yield来不断返回当前行，每次yield后暂停，下次迭代继续执行。
执行过程
初始row = [1]，yield输出第一行。
根据当前row生成next_row：
开头补1，结尾补1
中间元素通过row[i] + row[i+1]计算得到
row更新为next_row，循环往复。
"""
def triangles():
    row = [1]
    while True:
        yield row
        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)
        row = next_row

if __name__ == '__main__':
    n = 0
    for t in triangles():
        print(t)
        n += 1
        if n == 10:
            break