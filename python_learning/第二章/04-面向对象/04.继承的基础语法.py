# 演示单继承
class Phone:
    IMEI = None   #序列号
    producer = "LJ"
    def call_by_4g(self):
        print("4g通话")

class NFCReader:
    nfc_type = "第五代"
    producer = "LJ"
    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC读卡")

class Phone2022(Phone):
    face_id = 100001   #面容ID
    def call_by_5g(self):
        print("5g通话")

# 多继承   多继承中,如果父类有同名方法或属性,先继承的优先级高于后继承
class MyPhone(Phone2022,NFCReader):
    pass

phone = Phone2022()
phone.call_by_4g()
print(phone.producer)

phone = MyPhone()
phone.call_by_5g()
phone.write_card()
