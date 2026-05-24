# # 打开文件,不存在的文件
# fa = open("D:/test2.txt","a",encoding="utf-8")
# # # write写入
# fa.write("面向对象规范 ✅")
#
# # # flush刷新
# fa.flush()
#
# # # close关闭
# fa.close()

# 打开一个存在的文件,文件存在,会在原有内容后面继续写入
fa = open("D:/test2.txt","a",encoding="utf-8")

# write写入,flush刷新
fa.write("面向对象规范 ✅类设计正确 ✅添加 / 修改 / 删除 / 查询 全部正常 ✅不会崩溃 ✅符合题目所有要求 ✅可直接交作业 ✅")
fa.flush()
# close关闭
fa.close()

