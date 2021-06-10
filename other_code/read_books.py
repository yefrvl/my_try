B = []
with open('books.txt') as f:
    A = f.read().splitlines()

for i in A:
    B.append(i[0] + str(len(i)))



print('\n'.join(B))