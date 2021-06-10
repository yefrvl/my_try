from collections import Counter

a = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''

a1 = ['i', 'was', 'three', 'near']

b = Counter(a.lower().split())

c = {}
for x in a1:
    if x in b:
        print(x)

#print([x for x in a.lower().split()])
