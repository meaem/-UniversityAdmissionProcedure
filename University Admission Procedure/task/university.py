from collections import defaultdict

DEPARTMENT_LIST = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
department_exam = {"Biotech": [0, 1], "Chemistry": [1], "Engineering": [2, 3], "Mathematics": [2], "Physics": [0, 2]}


def get_mean(exam_scores, which):
    m = 0
    for i in range(len(which)):
        m += exam_scores[which[i]]

    return m / len(which)


def get_best(exam_scores, which):
    return max(get_mean(exam_scores, which), exam_scores[-1])


def main():
    m = int(input())
    students = []
    departments = defaultdict(list)
    with open('applicants.txt', 'r') as f:
        for line in f:
            x, y, phy, chem, math, cs, adm, u1, u2, u3 = line.split()
            students.append((f"{x} {y}", (float(phy), float(chem), float(math), float(cs), float(adm)), (u1, u2, u3)))
    for i in range(3):
        students.sort(key=lambda ss: (ss[2][i], -get_best(ss[1], department_exam[ss[2][i]]), ss[0]))
        not_qualified = []
        while len(students) > 0:
            stu = students.pop(0)
            u = stu[2][i]
            if len(departments[u]) < m:
                departments[u].append(stu)
            else:
                not_qualified.append(stu)
        students = [] + not_qualified

    for department in DEPARTMENT_LIST:
        student_list = departments[department]
        student_list.sort(key=lambda stu: (- get_best(stu[1], department_exam[department]), stu[0]))
        with open(f'{department}.txt', 'w') as f:
            for s in student_list:
                f.write(f"{s[0]} {get_best(s[1], department_exam[department])}\n")


main()
