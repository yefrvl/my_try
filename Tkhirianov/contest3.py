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

    return sum_value

def create_dict_sum_values(sum_value_dict):
    for student_id, student_value in sum_value_dict.items():
        sum_value_dict[student_id] = elements_value(student_value)
    return sum_value_dict


def sort_dict(sum_value_dict):

    sum_value_list = []

    for item in sum_value_dict:
        sum_value_list.append(sum_value_dict.items)

  """  for student_id, student_value in sum_value_dict:
        str_values = ','.join([str(x) for x in sorted(student_value, reverse=True)])
        print(f'Студент №{student_id}: {student_value}')"""





input_data(inp_data)
sort_dict(create_dict_sum_values(create_dict(A)))


