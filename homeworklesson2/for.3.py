students_marks = [
    {
        'school_class': '4a', 
        'scores':[3, 4, 4, 5, 2]
    },
    {
        'school_class': '4b', 
        'scores':[3, 4, 2, 5, 5]
    }
]
marks_a = 0
marks_len = 0
for marks in students_marks:
    marks_avg = sum(marks['scores']) / len(marks['scores'])
    marks_a = sum(marks['scores']) + marks_a
    marks_len = len(marks['scores']) + marks_len
    print(marks_avg)
print(marks_a / marks_len)


#sum(students_marks[0]['scores']) / len(students_marks[0]['scores'])
#sum(students_marks[1]['scores']) / len(students_marks[1]['scores'])