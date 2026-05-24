# year = int(input("请输入一个年份:"))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")


a = int(input("请输入第一个三角形的边长:"))
b = int(input("请输入第二个三角形的边长:"))
c = int(input("请输入第三个三角形的边长:"))

if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("这个三角形是等边三角形")
    elif a == b or b == c or a == c:
        print("这个三角形是等腰三角形")
    else:
        print("普通三角形")
else:
    print("这三条边不能构成三角形")