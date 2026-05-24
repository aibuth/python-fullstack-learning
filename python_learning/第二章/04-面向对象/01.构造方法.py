# # 1.设计一个类
# class Student:
#     def __init__(self,name,gender,nationality):
#         self.name = name
#         self.gender = gender
#         self.nationality = nationality
# # 2.创建一个对象# 对象属性进行赋值
# stu_1 = Student("阿贡","男","中国")
# # 获取对象中记录的信息
# print(stu_1.name)
# print(stu_1.gender)
# print(stu_1.nationality)



class Student:
    def __init__(self, name,age,addr):
        self.name = name
        self.age = age
        self.addr = addr

if __name__ == '__main__':
    for s in range(10):
        print(f"当前录入第{s + 1}为学生的信息:")
        name = input(f"请输入第{s + 1}位学生的姓名:")
        age = int(input(f"请输入第{s + 1}位学生的年龄:"))
        addr = input(f"请输入第{s + 1}位学生的地址:")
        stu = Student(name,age,addr)
        print(f"第{s + 1}位学生的信息录入完毕")
















