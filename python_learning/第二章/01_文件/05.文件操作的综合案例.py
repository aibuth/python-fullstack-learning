"""
读取文件
将文件写出到 bill.txt.bak 文件作为备份
同时，将文件内标记为测试的数据行丢弃
"""
fr = open("D:/bill.txt","r",encoding="utf-8")

fw = open("D:/bill.txt.bak","w",encoding="utf-8")

for line in fr:
    line = line.strip()
    if line.split(", ")[4] == "测试":
        continue
    fw.write(line)
    fw.write("\n")

fr.close()
fw.close()