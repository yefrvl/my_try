
list_ = [[0, 2], [0, 3], [0, 5], [1, 2], [1, 4], [1, 5], [2, 2], [2, 5], [2, 1]]

data = {}

for student_id, student_value in list_:
    data.setdefault(str(student_id), [])
    data[str(student_id)].append(student_value)


for student, values in data.items():
    str_values = ','.join([str(x) for x in sorted(values, reverse=True)])
    print(f'Студент №{student}: {str_values}')