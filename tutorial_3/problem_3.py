import math


marks = (35, 40, 50, 60, 80, 88, 20, 40, 75, 99)
no_of_A = 0
no_of_B = 0
no_of_C = 0
no_of_D = 0

average = sum(marks) / len(marks)
variance = 0
for mark in marks:
    variance += (mark - average) ** 2
    if mark < 50:
        no_of_D += 1
        continue
    if mark < 60:
        no_of_C += 1
        continue
    if mark < 80:
        no_of_B += 1
        continue
    if mark < 100:
        no_of_A += 1
        continue
variance /= len(marks)

print(
    f"""
*** Analysis of Student Marks ***
A : {no_of_A}
B : {no_of_B}
C : {no_of_C}
D : {no_of_D}
Average = {average}
Variance = {round(variance,2)}
Standard Deviation = {round(math.sqrt(variance),2)}
*** End ***
"""
)
