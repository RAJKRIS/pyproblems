"""
Program to find transpose
"""

a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]  # input
#b = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]  # expected output

final = []
for k, item in enumerate(a):
    temp = ()
    for l, j in enumerate(item):
        temp += (a[l][k],)
    final.append(temp)

print ("Input: ", a)
print ("Output: ", final)
