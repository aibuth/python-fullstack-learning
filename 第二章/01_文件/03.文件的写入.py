# 打开文件,不存在的文件
# fw = open("D:/test.txt","w",encoding="utf-8")
#
# # write写入
# fw.write("面向对象规范 ✅")
#
# # flush刷新
# fw.flush()
#
# # close关闭
# fw.close()        #close内置了flush的功能

# 打开一个存在的文件
fw = open("D:/test.txt","w",encoding="utf-8")

# write写入,flush刷新
fw.write("面向对象规范 ✅类设计正确 ✅添加 / 修改 / 删除 / 查询 全部正常 ✅不会崩溃 ✅符合题目所有要求 ✅可直接交作业 ✅")
fw.flush()
# close关闭
fw.close()

