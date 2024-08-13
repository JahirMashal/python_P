student = [("Alice", 85), ("Bob", 75), ("Charlie", 95)]

for i in range(len(student)):
    for j in range(0, len(student) -i -1):
        if student[j][1] < student[j + 1][1]:
            student[j], student[j + 1] = student[j + 1], student[j]
            
            
print(student)