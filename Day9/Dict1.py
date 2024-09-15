student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
keys = list(student_scores.keys())
values = list(student_scores.values())

#print(values)
#print(keys)
#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key, value in student_scores.items():

    if 91 < value <= 100:
        value = "Outstanding"
    elif 81 <= value <= 90:
        value = "Exceeds Expectations"
    elif 71 <= value <= 80:
        value = "Acceptable"
    else:
        value ="Fail"

    student_grades[key] = value


# 🚨 Don't change the code below 👇
print(student_grades)
