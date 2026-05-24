# while True:
#     username = input("请输入正确的用户名:")
#     password = input("请输入正确的密码:")
#     if username == "" or password == "":
#         print("输入的用户名或密码不能为空!")
#         continue
#     if username == "admin" and password == "123456":
#         print("登陆成功!进入B站首页~")
#         break
#     elif username == "zhangsan" and password == "444555666":
#         print("登陆成功!进入B站首页~")
#         break
#     elif username == "lisi" and password == "159357":
#         print("登陆成功!进入B站首页~")
#         break
#     else:
#         print("用户名或密码错误,请重新输入!")


num = 0
max_attempts = 5
while num < max_attempts:
    username = input("请输入正确的用户名:")
    password = input("请输入正确的密码:")
    num += 1
    sheng = max_attempts - num
    if username == "" or password == "":
        print("输入的用户名或密码不能为空!")
        continue
    if username == "admin" and password == "123456":
        print("登陆成功!进入B站首页~")
        break
    elif username == "zhangsan" and password == "444555666":
        print("登陆成功!进入B站首页~")
        break
    elif username == "lisi" and password == "159357":
        print("登陆成功!进入B站首页~")
        break
    else:
        print("用户名或密码错误,请重新输入!")
    if sheng > 0:
        print(f"您还剩{sheng}次机会")
    else:
        print("登陆失败!!!")









