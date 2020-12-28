A = []
inp_data = input()

def input_data(inp_data):
    while inp_data != '#':

        A.append(inp_data)
        inp_data = input()


def sort(A):
    for k in A:
        if len(k) <= 2:
            A.remove(k)

    for i in range(1,len(A)+1):
        for j in range(1):
            if j[0] == i[i-1][0]:
                i[j-1] + i[j]

    A.sort(key=lambda x: max((x[-1])))
    return A





input_data(inp_data)



sort(A)

print(A)