students_grades_dict = {}
student_grade_count = int(input())
for student in range(student_grade_count):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_grades_dict.keys():
        students_grades_dict[student_name] = []
    students_grades_dict[student_name].append(student_grade)
for student, grade in students_grades_dict.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
