class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"学生的姓名为:{self.name},年龄为:{self.age}"

    # def __lt__(self,other):
    #     return self.age < other.age

    # def __le__(self,other):
    #     return self.age <= other.age

    def __eq__(self,other):
        return self.age == other.age

stu1 = Student("阿文",20)
print(stu1)

stu2 = Student("阿凯",20)
print(stu1 == stu2)

