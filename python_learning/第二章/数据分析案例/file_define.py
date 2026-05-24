"""
和文件相关的类定义
"""
from date_define import Record
import json

# 先定义一个抽象类用来做顶层设计,确定有哪些功能需要实现
class FileReader:
    def read_date(self) -> list[Record]:
        pass

class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path           #定义成员变量记录文件的路径

#     复写(实现抽象方法)父类的方法
    def read_date(self) -> list[Record]:
        with open(self.path,"r",encoding="UTF-8") as f:
            record_list: list[Record]  =[]
            for line in f.readlines():
                line = line.strip()

                date_list = line.split(",")
                record = Record(date_list[0],date_list[1],int(date_list[2]),date_list[3])
                record_list.append(record)

        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_date(self) -> list[Record]:
        with open(self.path,"r",encoding="UTF-8") as f:
            record_list: list[Record]  =[]
            for line in f.readlines():
                date_dict = json.loads(line)
                record = Record(date_dict["date"],date_dict["order_id"],int(date_dict["money"]),date_dict["province"])
                record_list.append(record)
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
    list1 = text_file_reader.read_date()

    json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")
    list2 = json_file_reader.read_date()

    for l in list1:
        print(l)
    for l in list2:
        print(l)
