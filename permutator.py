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
    if n > 20:
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
    maxLengths=[1,2,3,4,6,6,12,15,20,30,30,60,60,84,105,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
    with open("output.txt", "w") as file:
        for n in range(20):
            for m in range(maxLengths[n]):
                c = sort_combinations(n+1,m+1)
                file.write(f'Subloops for {n+1}-permutator with loop length {m+1}:\n')
                for i in c:
                    txt = ''
                    for j in i:
                        txt += f'{j}  '
                    file.write(txt + "\n")
                file.write('\n')

def investigation(n,m):
    c = sort_combinations(n,m)
    total = 0
    for i in c: # possible combinations of subloops
        cnts = [0] * 21
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
    maxLengths=[1,2,3,4,6,6,12,15,20,30,30,60,60,84,105,1000,1000,1000,1000,1000,1000,1000,1000,1000]
    with open("output.txt", "w") as file:
        for m in range(maxLengths[n-1]):
            output = investigation(n,m+1)
            file.write(f'{int(output)}\n')
            print(int(output))

allPermutators(15)
#print(investigation(8,5))
#findAllSubloops()