
from collections import defaultdict

DEPARTMENT_LIST = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]


department_exam = {"Biotech":1, "Chemistry":1, "Engineering":3, "Mathematics":2, "Physics":0}

def main():
    # n, m = int(input()), int(input())  # int()
    # m = input()  # int()
    # print(f"*{n}*{m}*")
    # students = [(f"{x} {y}", z) for _ in range(1) for x, y, z in input().split()]
    m = int(input())
    students = []
    departments = defaultdict(list)
    with open('applicants.txt', 'r') as f:
        for line in f:
            x, y, phy, chem, math, cs, u1, u2, u3 = line.split()
            students.append((f"{x} {y}", (float(phy), float(chem), float(math), float(cs)), (u1, u2, u3)))
            # departments.setdefault(u1, []).append(student)
            # departments[u1] += 1
    # departments = sorted(departments,key=lambda x:x[0])
    # for s in students:
    #     print(s)

    for i in range(3):
        # dept = ss[2][i]
        # exam =department_exam[dept]
        students.sort(key=lambda ss: (ss[2][i],-ss[1][department_exam[ss[2][i]]],  ss[0]))
        # for s in students:
        #     print("*******",s)
        not_qualified = []
        while len(students) > 0:
            stu = students.pop(0)
            u = stu[2][i]
            # print(stu)
            if len(departments[u]) < m:  # and departments[u1]) < m:
                departments[u].append(stu)
            else:
                not_qualified.append(stu)
            # elif len(departments[u2]) < m:  # and departments[u1]) < m:
            #     departments[u2].append(stu)
            # elif len(departments[u3]) < m:  # and departments[u1]) < m:
            #     departments[u3].append(stu)
        students = [] + not_qualified
        # for s in students:
        #     print("-----",s)
    # print(departments)

    for department in DEPARTMENT_LIST:
        student_list = departments[department]
        student_list.sort(key=lambda stu: (-stu[1][department_exam[department]], stu[0]))
        print(department)
        # selected = student_list[:m]
        for s in student_list:
            print(f"{s[0]} {s[1][department_exam[department]]}")

        print()


main()
