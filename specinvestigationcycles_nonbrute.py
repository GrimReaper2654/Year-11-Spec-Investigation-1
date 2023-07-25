from itertools import permutations
import string
from math import lcm, factorial

def find_combinations(n, max_num=None):
    if max_num is None:
        max_num = n
    if n == 0:
        return [[]]
    elif max_num == 1:
        return [[1]*n]
    else:
        combinations = []
        for i in range(1, max_num+1):
            if i <= n:
                sub_combinations = find_combinations(n-i, min(i, n-i))
                for sub_combination in sub_combinations:
                    combinations.append([i] + sub_combination)
        return combinations

def choose(n,r):
    return (factorial(n)) // (factorial(r) * (factorial(n-r)))

def calculate_combinations(n, l):
    now_n = n
    total = 1
    for i in l:
        if i == 1:
            continue
        total *= choose(now_n, i) * factorial(i - 1)
        now_n -= i
    temp_max_repeat = [l.count(x) if x != 1 else 0 for x in set(l)]
    max_repeat = max(temp_max_repeat)
    divisor = 1
    for item in temp_max_repeat:
        if item == 0:
            continue
        divisor *= factorial(item)  
    return total // divisor

'''
n = 13
adds = find_combinations(n)
all_lengths = {}
max_lcm = 0
for item in adds:
    if lcm(*item) == 6:
        print(calculate_combinations(n, item))
        print(item)
    if lcm(*item) in all_lengths.keys():
        all_lengths[lcm(*item)] += calculate_combinations(n, item)
    else:
        all_lengths[lcm(*item)] = calculate_combinations(n, item)
'''

'''
sorted_d = sorted(all_lengths.keys())
print(f"for {n = }")
out = open("./mathout.txt", "w")
total_sum = 0
for i in range(1, max(sorted_d) + 1):
    if i in sorted_d:
        k = i
    else:
        out.write("0\n")
        continue
    print(f"    for loop length {k} there is {all_lengths[k]}")
    out.write(str(all_lengths[k]) + "\n")
    total_sum += all_lengths[k]

print(f"{total_sum = } {factorial(n) = }")

out.close()
'''



'''
#loop length, how many there are
for n in range(1, 16):
    adds = find_combinations(n)
    all_lengths = {}
    max_lcm = 0
    for item in adds:
        if lcm(*item) in all_lengths.keys():
            all_lengths[lcm(*item)] += calculate_combinations(n, item)
        else:
            all_lengths[lcm(*item)] = calculate_combinations(n, item)

    sorted_d = sorted(all_lengths.keys())
    print(f"for {n = }")
    for k in sorted_d:
        print(f"    for loop length {k} there is {all_lengths[k]}")
'''



'''
# loop lengths and their internal loops
for n in range(1, 16):
    adds = find_combinations(n)
    lengths = {}
    max_lcm = 0
    for item in adds:
        if lcm(*item) in lengths.keys():
            lengths[lcm(*item)].append(item)
        else:
            lengths[lcm(*item)] = [item]

    out = open("./mathout.txt", "w")
    print(f"{n = } has internal loops:")
    for k,v in lengths.items():
        print("    " + f"loop length: {k} has internal loops {v}")
'''




'''
# which loop lengths n has
for n in range(7, 7):
    adds = find_combinations(n)
    lengths = []
    max_lcm = 0
    for item in adds:
        lengths.append(lcm(*item))

    print(f"{n = } has loop lenghts {set(lengths)}")

'''

'''

# find max loop length
for n in range(1, 15):
    adds = find_combinations(n)
    max_lcm = 0
    for item in adds:
        if lcm(*item) > max_lcm:
            max_lcm = lcm(*item)

    print(f"{n = } has a max loop length of {max_lcm}")
'''