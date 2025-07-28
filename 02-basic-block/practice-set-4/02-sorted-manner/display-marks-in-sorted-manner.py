
## write a program to accept marks of 6 students and display them in a sorted manner ## 

marks = []

for i in range(6):
    marks_input = int(input(f"enter marks {i + 1} : "))

    marks.append(marks_input)

sorted_marks = sorted(marks)

print(sorted_marks)
