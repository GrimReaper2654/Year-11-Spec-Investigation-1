'''
import itertools
import time
import math

def get_permutations(nums):
    return itertools.permutations(nums)

def findPermutators(n, m):
    seq = [i+1 for i in range(n)]
    seq2 = seq.copy()
    nseq = seq.copy()

    permutations = get_permutations(nseq)
    p = math.factorial(n)
    print('Got all permutations...')
    cnt = 0
    with open('output.txt', 'w') as f:
        for i, perm in enumerate(permutations):
            t = 0
            while True:
                newseq = seq.copy()
                for j in range(n):
                    newseq[perm[j]-1] = seq[j]
                seq = newseq
                t += 1
                if seq == seq2:
                    if t == m:
                        cnt += 1
                    break
            if i % 1 == 0:
                output_str = f'Processed {i} / {p} permutations\n'
                print(output_str, end='')
        output_str = f'\nTotal Possibilities: {cnt}\n'
        print(output_str)
        f.write(str(cnt))

def massPermutator(n):
    seq = [i+1 for i in range(n)]
    seq2 = seq.copy()
    nseq = seq.copy()

    permutations = get_permutations(nseq)
    p = math.factorial(n)
    print('Got all permutations...')
    cnt = [0]*105
    with open('output.txt', 'w') as f:
        for i, perm in enumerate(permutations):
            t = 0
            while True:
                newseq = seq.copy()
                for j in range(n):
                    newseq[perm[j]-1] = seq[j]
                seq = newseq
                t += 1
                if seq == seq2:
                    cnt[t-1]+=1
                    break
            if i % 10 == 0:
                output_str = f'Processed {i} / {p} permutations\n'
                print(output_str)
        output_str = f'\nTotal Possibilities: \n'
        print(output_str)
        for i in cnt:
            print(i)
            f.write(str(i)+'\n')

n = 13
m = 9

start_time = time.time()
#findPermutators(n,m) # output is total numeber of permutators
massPermutator(n) # mass permutator output is loop length 0, loop length 1, loop length 2, loop length 3, ... , loop length 105
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time: {round(elapsed_time*1000)}ms\n")
'''
'''
from itertools import permutations
import string
from math import lcm, factorial

def findCombinations(n):
    if n == 0:
        return [[]]
    else:
        combinations = []
        for i in range(1,n):
            if i <= n:
                subCombinations = findCombinations(n-1, min(i, n-i))
                for subCombination in subCombinations:
                    combinations.append([i]+subCombination)
        return combinations

def choose(n, r):
    return (factorial(n) // (factorial(r)*factorial(n-r)))

def calculateCombinations(n, m):
    nowN = n
    total = 1
    for i in m:
        if i == 1:
            continue
        total *= choose(nowN, i) * factorial(i-1)
        nowN -= 1
    maxRepeat = max([m.count(x) if x != 1 else 0 for x in m])
    return total // factorial(n)

n=10
adds = findCombinations(n)
allLenghts = {}
maxLCM = 0
for item in adds:
    if lcm(*item) in allLenghts.keys():
        allLenghts[lcm(*item)] += calculateCombinations(n, item)
    else:
        allLenghts[lcm(*item)] = calculateCombinations(n, item)

sorted_d = sorted(allLenghts.keys())
print(f'for {n = }')
totalSum = 0
for i in range(1, max(sorted_d) + 1):
    if i in sorted_d:
        k=i
'''
from math import gcd, factorial

def get_combinations(n):
    if n == 0:
        return [[]]
    table = [[] for _ in range(n+1)]
    table[0] = [[]]
    for i in range(1, n+1):
        for j in range(i, n+1):
            for combo in table[j-i]:
                table[j].append([i] + combo)
    return table[n]

def lcm(numbers):
    if len(numbers) == 0:
        return 1
    elif len(numbers) == 1:
        return numbers[0]
    else:
        result = numbers[0]
        for i in range(1, len(numbers)):
            result = result * numbers[i] // gcd(result, numbers[i])
        return result

def sort_combinations(n, m):
    if n > 15:
        return "Error: n is greater than 15"
    else:
        combinations = get_combinations(n)
        combinations_m = [combo for combo in combinations if lcm(combo) == m]
        return combinations_m

def nCr(n, r, memo={}):
    """
    This function takes in two integers n and r and returns the number of ways to choose r items from a set of n items,
    also known as n choose r or the binomial coefficient.
    """
    if not isinstance(n, int) or not isinstance(r, int) or n < 0 or r < 0 or r > n:
        # Check if n and r are both integers and n >= r >= 0
        raise ValueError("n and r must be non-negative integers with n >= r.")
    if r > n // 2:
        # Use symmetry of nCr to reduce computation time
        r = n - r
    if r == 0:
        # Base case
        return 1
    if (n, r) in memo:
        # Use memoization to avoid redundant calculation
        return memo[(n, r)]
    result = nCr(n-1, r-1, memo) * n // r
    memo[(n, r)] = result
    return result

def findAllSubloops():
    maxLengths=[1,2,3,4,6,6,12,15,20,30,30,60,60,84,105]
    with open("output.txt", "w") as file:
        for n in range(15):
            for m in range(maxLengths[n]):
                c = sort_combinations(n+1,m+1)
                file.write(f'Subloops for {n+1}-permutator with loop length {m+1}:\n')
                for i in c:
                    txt = ''
                    for j in i:
                        txt += f'{j}  '
                    file.write(txt + "\n")
                file.write('\n')

def investigaytion(n,m):
    c = sort_combinations(n,m)
    total = 0
    for i in c: # possible combinations of subloops
        cnts = [0] * 16
        for j in i: # each individual subloop
            cnts[j] += 1
        cn = n
        subtotal = 1
        for sl in range(2,len(cnts)):
            if (cnts[sl] > 0): # subloops of length sl exist
                if(cnts[sl] == 1): # exactly 1 of a subloop
                    subtotal *= nCr(cn,sl)*factorial(sl-1)
                    cn -= sl
                else:
                    subsubtotal = 1 # ik this is not necessary but it looks nicer this way
                    for anotherVariable in range(cnts[sl]):
                        subsubtotal *= nCr(cn,sl)*factorial(sl-1)
                        cn -= sl
                    subsubtotal /= factorial(cnts[sl])
                    subtotal *= subsubtotal
        total += subtotal
    return total


def allPermutators(n):
    maxLengths=[1,2,3,4,6,6,12,15,20,30,30,60,60,84,105]
    with open("output.txt", "w") as file:
        for m in range(maxLengths[n-1]):
            output = investigaytion(n,m+1)
            file.write(f'{int(output)}\n')
            print(int(output))

#allPermutators(15)
findAllSubloops()