# write your code here
def main():
    n, m = int(input()), int(input())  # int()
    # m = input()  # int()
    # print(f"*{n}*{m}*")
    # students = [(f"{x} {y}", z) for _ in range(1) for x, y, z in input().split()]
    students = []
    for _ in range(n):
        x, y, z = input().split()
        students.append((f"{x} {y}", float(z)))
        # print(students)
    students.sort(key=lambda x: (-x[1], x[0]))
    selected = students[:m]
    print("Successful applicants:")
    for s in selected:
        print(s[0])


main()
# 5
# 3
# Cole Collins 3.68
# Dolores Baldwin 3.40
# Brett Boyer 2.45
# Nora Alston 3.71
# Jessy Moore 3.14
