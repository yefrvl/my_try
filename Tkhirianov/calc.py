A = []
B = []
x = (input('Ввеедите задачу: '))
for x in x:
    A.append(x)
for x in A:
    if x == " ":
        A.remove(x)
summ_dec = 0
time_int = 0
for x in A:
    if x.isdecimal():
        time_int = int(x)
    else:
        z = ''
        if x == '+':
            summ_dec += time_int
        elif x == '-':
            summ_dec -= time_int
        elif x == '*':
            summ_dec *= time_int
        elif x == '/':
            if time_int != 0:
                summ_dec /= time_int
            else:
                print('нельзя')

print(summ_dec)














