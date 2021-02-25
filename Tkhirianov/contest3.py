A = []
inp_data = input()

def input_data(inp_data : int):
    while inp_data != '#':
        A.append(inp_data.split(' '))
        inp_data = input()

def elements_value(spis_value):
    theSum = 0
    for element in spis_value:
        theSum = theSum + int(element)
    return theSum

def create_dict(A : list):
    sum_value = {}
    for student_id, student_value in A:
        sum_value.setdefault(str(student_id), [])
        sum_value[str(student_id)].append(student_value)
    new_sum_value1 = sum_value.copy()
    new_sum_value = (sort_sum_dict(create_dict_sum_values(sum_value)))
    print(new_sum_value, new_sum_value1)


def create_dict_sum_values(sum_value_dict):
    for student_id, student_value in sum_value_dict.items():
        sum_value_dict[student_id] = elements_value(student_value)
    return sum_value_dict

def sort_sum_dict(sum_value_dict):
    sum_value_list = sum_value_dict.items()

    return sorted(sum_value_list, key=lambda x: x[1], reverse=True)








input_data(inp_data)
create_dict(A)


