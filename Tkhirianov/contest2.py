A = []
x = input()

def createMassiv(x):
    while x != '#':
        A.append(x)
        x = input()
    return A

def average (A):
    y = 0
    for i in A:
        y += int(i)
    y /= len(A)
    return round(y, 3)

def summBalances (A):
    B = []
    for i in A:
        while int(i) % 3 != 0:
                z = 0
                z += int(i)
        B.append(z)
        i+=1


    return z







createMassiv(x)
summBalances(A)
# average(A)

print(summBalances(A))




