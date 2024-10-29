# Alexander Williams
# 10/29/2024
# Web and app development

student_names = []
student1 = input('What is the first students name?:\n')
student2 = input('What is the second students name?:\n')
student3 = input('What is the third students name?:\n')
student4 = input('What is the fourth students name?:\n')

student_names.append(student1)
student_names.append(student2)
student_names.append(student3)
student_names.append(student4)


student1_scores = [90,95,100,98]
student2_scores = [70,65,68,79]
student3_scores = [85,90,88,91]
student4_scores = [50,60,55,58]

student1_average = sum(student1_scores) / len(student1_scores)
student2_average = sum(student2_scores) / len(student2_scores)
student3_average = sum(student3_scores) / len(student3_scores)
student4_average = sum(student4_scores) / len(student4_scores)








print(f'Student: {student1}')
print('School: RedCrest highschool')
print('Course: Algebra')
print(f'Average score: {student1_average}')