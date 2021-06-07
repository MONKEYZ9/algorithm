N = int(input())

dataN = []
for i in range(N):
    input_data = input().split()
    dataN.append((input_data[0], int(input_data[1])))

dataN = sorted(dataN, key=lambda student : student[1])

for student in dataN:
    print(student[0], end= ' ')