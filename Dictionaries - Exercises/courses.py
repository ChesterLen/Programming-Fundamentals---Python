courses_count = int(input())
courses_list = []
for course in range(1, courses_count + 1):
    course_name = input()
    courses_list.append(course_name)
print(courses_list)
