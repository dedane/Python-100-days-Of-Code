# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
highest_score = student_scores[0]

for i in student_scores:
  if i > highest_score:
    highest_score = i

print(f' this is the highest score: {highest_score}')
