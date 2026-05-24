fr = open("D:/word.txt","r",encoding = "UTF-8")

# 方式1:读取全部内容,通过字符串count统计itheima出现的次数
# content = fr.read()
# count = content.count("itheima")
# print(f"itheima出现的次数为:{count}")

# 方式2:读取内容,一行一行读取
count = 0
for line in fr:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1
print(f"itheima出现的次数是:{count}")

fr.close()