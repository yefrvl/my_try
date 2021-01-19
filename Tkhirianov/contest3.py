A = []
B = []
inp_data = input()


def input_data(inp_data):
    while inp_data != '#':
        A.append(inp_data.split(' '))
        inp_data = input()


def sort(A):
    amount = 0  # количество студентов
    for k in A:
        if len(k) < 2:
            amount = int(k[0])
            A.remove(k)

    p = 1   # счетчик студентов
    c = 0   # суммарный бал студентов
    for i in (A):
        if p <= amount:
            if int(i[0]) == p:
                c += int(i[1])
            else:
                p+=1
                B.append(c)
                c = 0
    return B


# A.sort(key=lambda x: max((x[-1])))
# return A


input_data(inp_data)

sort(A)

print(A, B)
