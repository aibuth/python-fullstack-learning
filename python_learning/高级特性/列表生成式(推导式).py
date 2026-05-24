print([x * x for x in range(1,11)])

print([x * x for x in range(1,11) if x % 2 == 0])

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in "ABC" for n in "XYZ"])

import os   # 导入os模块
print([d for d in os.listdir('.')])     # os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k,v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
"""
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = ???

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
"""
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str) == True]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')




