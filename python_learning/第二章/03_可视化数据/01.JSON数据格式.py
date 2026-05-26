import json
# 准备列表,列表里面都是字典,将其转换为JSON
data = [{"name":"张大山","age":"18"},{"name":"王大锤","age":20},{"name":"刘洋","age":30}]
data_str = json.dumps(data,ensure_ascii=False)
print(type(data_str))
print(data_str)
# 准备字典,将字典转换为JSON
d = {"name":"周杰轮","addr":"台北"}
a_ste = json.dumps(d,ensure_ascii=False)
print(type(a_ste))
print(a_ste)
# 将JSON字符串转换为Python数据类型
s = '[{"name":"张大山","age":"18"},{"name":"王大锤","age":20},{"name":"刘洋","age":30}]'
l = json.loads(s)
print(type(l))
print(l)

s = '{"name":"周杰轮","addr":"台北"}'
d = json.loads(s)
print(type(d))
print(d)




