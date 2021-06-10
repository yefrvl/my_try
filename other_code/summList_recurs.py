def sumList(x, i=0):
    if i >= len(x):
        return 0
    else:
        return x[i] + sumList(x, i+1)


print(sumList([5, 5, 5, 5, 5, 5]))