# 🚨 Don't change the code below 👇
student_height = input("Input a list of student scores ").split()
for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
print(student_height)
score = 0
for i, student_score in enumerate(student_height):
    score += student_score
print(f'The average height of the students is: {score / len(student_height)}')
# 🚨 Don't change the code above 👆
#  print(f'The average height of all the students, is {sum(student_heights[n]) / len(student_heights[n])}')



#Write your code below this row 👇

