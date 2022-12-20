import matplotlib.pyplot as plt
import random


def calculate_lcm(x, y) -> int:
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if(greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


def find_min_lcm_pair(n: int):
    response = n
    simple_list = [x for x in range(1, n // 2)]

    for simple in simple_list:
        if (n % simple == 0) and (response > n // simple):
            response = n // simple
    return n // response, n - n // response


n = int(input())

print(find_min_lcm_pair(n))

'''''
x = []
lcm = []

for i in range(1, n // 2):
    x.append(i)
    lcm.append(calculate_lcm(i, n - i))

min = lcm[0]
min_index = 0

for l in lcm:
    if l < min:
        min = l

min_index = lcm.index(min)

print(min, x[min_index], n - x[min_index])
plt.plot(x, lcm)
plt.show()
'''''