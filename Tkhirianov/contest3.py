A = []
inp_data = input()

def input_data(inp_data):
    while inp_data != '#':
        A.append(inp_data)
        inp_data = input()


def sort(A):



    A.sort(key=lambda x: max((x[-1])))

input_data(inp_data)



sort(A)

print(A)