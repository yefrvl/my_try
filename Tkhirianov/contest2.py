A = []
x = input()


def find_inp(x):
    if x.isdigit():
        createMassiv(x)
    else:
        global A
        A = list(map(int, x.split()))



def createMassiv(x):
    while x != '#':
        x = int(x)
        A.append(x)
        x = input()
    return A

def average(A):
    y = 0
    for i in A:
        y += int(i)
    y /= len(A)
    return round(y, 3)

def summBalances (A):
    while len(A) % 3 != 0:
        A.append(1)
    n = 0
    while len(A) > 0:
        n += sum(A[:3]) % A[2]
        del A[:3]



    return n






find_inp(x)


print(average(A), max(A), min(A), summBalances(A))




