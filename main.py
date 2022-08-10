# 🚨 Don't change the code below 👇
import math
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
student_count = len(student_heights)
for student in student_heights:
  sum+=student

average_height = sum / student_count

print(f"Average height: {math.ceil(average_height)}")
print(f"Sum of heights: {sum}")

# total_height = sum(student_heights)
# print(total_height)

marks = [65, 71, 68, 74, 61]

# find sum of all marks
total_marks = sum(marks)
print(total_marks)
