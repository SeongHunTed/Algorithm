student = [0] * 31

for i in range(1, 29):
    person = int(input())
    student[person] = 1

for i in range(1, 31):
    if student[i] == 0:
        print(i)