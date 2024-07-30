n = int(input('Enter the number of students: '))
student_marks = {}
for i in range(n):
    name, *line = input("Enter student's name and scores: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input('Enter the name of the student to query: ')

if query_name in student_marks:
    total = sum(student_marks[query_name])
    avg = total / len(student_marks[query_name])
    print(f'{avg:.2f}')