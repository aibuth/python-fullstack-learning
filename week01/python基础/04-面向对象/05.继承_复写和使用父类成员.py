class Phone:
    IMEI = "None"
    producer = "YG"
    def call_by_5g(self):
        print("5g通话")

# 定义子类,复写父类成员
class NewPhone(Phone):
    IMEI = "12003"       #复写父类的成员属性
    producer = "YK"
    def call_by_5g(self):
        print("使用5g网络进行通话")

#         方式1
        print(f"父类的厂商为{Phone.producer}")
        Phone.call_by_5g(self)

#         方式2
        print(f"父类的厂商为{super().producer}")
        super().call_by_5g()
my_phone = NewPhone()
my_phone.call_by_5g()
print(my_phone.producer)