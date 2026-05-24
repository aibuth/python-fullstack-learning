# # 案例1：定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。
# def triangle_area(base,height):
#     """
#     根据传入的底和高计算三角形面积 v
#     :param base: 底
#     :param height: 高
#     :return: 三角形的面积
#     """
#     return (base * height) / 2
# print(triangle_area(20,10))
#
# # 案例2：定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
# def count_aeiou(s):
#     """
#     计算传入的字符串中元音字母的个数
#     :param s: 字符串
#     :return:元音字母的个数
#     """
#     num = 0
#     for w in s:
#         if w in "aeiouAEIOU":
#            num += 1
#     return num
# print(count_aeiou("Hello World Hello Python OK"))
#
# # 案例3：定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
# def calc_score(score_list):
#     s_max = max(score_list)
#     s_min = min(score_list)
#     s_avg = round(sum(score_list) / len(score_list),1)
#     return s_max, s_min, s_avg
# s_list = [564,598,642,630,647,598,483]
# s_max, s_min, s_avg = calc_score(s_list)
# print("最高分:", s_max)
# print("最低分:", s_min)
# print("平均分:", s_avg)


# 1.定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# - 分数 >= 90: A
# - 分数 >= 75: B
# - 分数 >= 60: C
# - 分数 < 60: D
# def grade_score(score):
#     """
#     根据传入的分数，计算对应的分数等级并返回
#     :param score: 分数
#     :return: 返回的等级
#     """
#     if score >= 90:
#         return "A"
#     elif 75 <= score < 90:
#         return "B"
#     elif 60 <= score <75:
#         return "C"
#     else:
#         return "D"
# print(grade_score(100))
# print(grade_score(85))
#
# # 2.定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# # - 把字符串反转，如果和原字符串相同，就是回文串。(如: "level", "radar", "黄山落叶松叶落山黄")
# def palindrome_str(str):
#     """
#     判断一个字符串是否是回文串
#     :param str: 字符串
#     :return: bool值
#     """
#     if str == str[::-1]:
#         return True
#     else:
#         return False
# print(palindrome_str("level"))
# print(palindrome_str("黄山落叶松叶落山黄"))
#
# # 3.定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
# def sec_to_time(seconds):
#     """
#     将传入的秒转换为小时、分钟、秒
#     :param seconds: 传入的总秒数
#     :return: 小时、分钟、秒
#     """
#     h = seconds // 3600
#     m = seconds % 3600 // 60
#     s = seconds % 60
#     return h,m,s
# h,m,s = sec_to_time(3665)
# print(f"{h}小时,{m}分钟,{s}秒")


# 4.定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
def if_triangle(l1,l2,l3):
    """
    根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）
    :param l1: 三角形的一条边
    :param l2: 三角形的一条边
    :param l3: 三角形的一条边
    :return: 三角形的类型（等边、等腰、普通，或者不能构成三角形）
    """
    if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
        if l1 == l2 == l3:
            return "等边三角形"
        elif l1 == l2 or l1 == l3 or l2 == l3:
            return "等腰三角形"
        else:
            return "普通三角形"
    else:
        return "不能构成三角形"
print(if_triangle(3,3,3,))
print(if_triangle(2,2,3))
print(if_triangle(4,5,6))
print(if_triangle(1,2,9))
