# 🚨 Don't change the code below 👇
student_height = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
score = 0
for i, student_score in enumerate(student_scores):
    score += student_score
print(f'The average height of the students is: {score / len(student_scores)}')
# 🚨 Don't change the code above 👆
#  print(f'The average height of all the students, is {sum(student_heights[n]) / len(student_heights[n])}')



#Write your code below this row 👇

