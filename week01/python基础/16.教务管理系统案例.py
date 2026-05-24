"""
练习：基于现有知识开发一个教务管理系统

开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
2.修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3.删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
4.查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5.列出所有学生：遍历所有学生信息并输出。
6.统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
7.退出系统。
"""


manage_students = {}
menu = """
# # # # # # # # # # # # # # # # # # # # # # # # 【菜 单】 # # # # # # # # # # # # # # # # # # # # # # # #
#      1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出系统      #    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
"""

while True:
    print(menu)

    choice = input("请输入要执行的操作(1-7):")
    match choice:
        case "1":   #添加学生信息
            student_name = input("请输入要添加的学生的姓名:")
            score_chinese = float(input("请输入要添加的学生的语文成绩:"))
            score_math = float(input("请输入要添加的学生的数学成绩:"))
            score_english = float(input("请输入要添加的学生的英语成绩:"))

            if student_name in manage_students:
                print("学生已添加,请重新选择")
            else:
                manage_students[student_name] = {"chinese":score_chinese,"math":score_math,"english":score_english}
                print("学生添加完成")

        case "2":   #修改学生信息
            student_name = input("请输入要修改的学生的姓名:")
            if student_name not in manage_students:
                print("该学生不存在,请重新选择")
                continue
            else:
                score_chinese = float(input("请输入要修改的学生的语文成绩:"))
                score_math = float(input("请输入要修改的学生的数学成绩:"))
                score_english = float(input("请输入要修改的学生的英语成绩:"))

                manage_students[student_name] = {"chinese": score_chinese, "math": score_math, "english": score_english}
                print("学生修改完成")

        case "3":   #删除学生信息
            student_name = input("请输入要删除的学生的姓名:")
            if student_name not in manage_students:
                print("该学生不存在,请重新选择")
            else:
                del manage_students[student_name]
                print("学生删除完成")

        case "4":   #查询学生信息
            student_name = input("请输入要查询的学生的姓名:")
            if student_name not in manage_students:
                print("学生不存在,请重新操作!")
            else:
                info = manage_students[student_name]
                print(f"学生姓名:{student_name},语文成绩:{info['chinese']},数学成绩:{info['math']},英语成绩:{info['english']}")


        case "5":   #列出所有学生
            for student_name in manage_students.keys():
                student_info = manage_students[student_name]
                print(f"学生姓名:{student_name},语文成绩:{student_info['chinese']},数学成绩:{student_info['math']},英语成绩:{student_info['english']}")

        case "6":   #统计班级成绩
            if not manage_students:
                print("暂无学生，无法统计")
                continue

            chinese = [s['chinese'] for s in manage_students.values()]
            math    = [s['math'] for s in manage_students.values()]
            english = [s['english'] for s in manage_students.values()]
            names = list(manage_students.keys())
            sum_name = len(names)

            # 语文
            c_max = max(chinese)
            c_min = min(chinese)
            c_avg = sum(chinese) / sum_name
            c_max_name = names[chinese.index(c_max)]
            c_min_name = names[chinese.index(c_min)]

            # 数学
            m_max = max(math)
            m_min = min(math)
            m_avg = sum(math) / sum_name
            m_max_name = names[math.index(m_max)]
            m_min_name = names[math.index(m_min)]

            # 英语
            e_max = max(english)
            e_min = min(english)
            e_avg = sum(english) / sum_name
            e_max_name = names[english.index(e_max)]
            e_min_name = names[english.index(e_min)]

            print("==========学生成绩统计==========")
            print(f"语文: 最高分:{c_max},最低分:{c_min},平均分:{c_avg:.1f},最高分的学员姓名:{c_max_name},最低分的学员姓名:{c_min_name}")
            print(f"数学: 最高分:{m_max},最低分:{m_min},平均分:{m_avg:.1f},最高分的学员姓名:{m_max_name},最低分的学员姓名:{m_min_name}")
            print(f"英语: 最高分:{e_max},最低分:{e_min},平均分:{e_avg:.1f},最高分的学员姓名:{e_max_name},最低分的学员姓名:{e_min_name}")

        case "7":   #退出系统
                print("教务管理系统已退出!")
                break
        case _:
                print("输入操作有误,请重新输入")



