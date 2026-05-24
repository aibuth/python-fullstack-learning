def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,"r",encoding="UTF-8")
        print(f.read())
    except Exception as e:
        print(f"出现异常了,问题是{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name,date):
    f = open(file_name,"a",encoding="UTF-8")
    f.write(date)
    print("\n")
    f.close()



# if __name__ == '__main__':
#     # print_file_info("D:/wordc.txt")
#     append_to_file("D:/abc.txt","111222333")