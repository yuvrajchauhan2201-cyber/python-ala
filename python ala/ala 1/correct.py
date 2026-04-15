print("Online Exam")

students = []
marks = []

for i in range(3):
    name = input("Enter name: ")
    m = float(input("Enter marks: "))   # Convert marks to float
    students.append(name)
    marks.append(m)

total = 0
for x in marks:
    total = total + x

avg = total / 3

print("Students:", students)
print("Average:", avg)

if avg > 50:
    print("Pass")
else:
    print("Fail")

for i in range(2):
    print("Finished")

print("Exit")