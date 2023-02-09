if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score, name])

    # print(students)
    students.sort()
    # print(students)

    lowest = students[0]
    lowests = []
    e = 0
    for student in students:
        if e == 1:
            if student[0] == lowests[0][0]:
                lowests.append(student)
        else:
            if student[0] > lowest[0]:
                e = 1
                lowests.append(student)
        
    for l in lowests:
        print(l[1])