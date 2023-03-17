'''
import itertools
import copy

def get_permutations(nums):
    return list(itertools.permutations(nums))

n = 9
nseq = []
for i in range(n):
    nseq.append(i+1)
seq = copy.deepcopy(nseq)

permutations = get_permutations(nseq)
print('Got all permutations...')
maxt = 0
with open('output.txt', 'w') as f:
    for perm in permutations:
        t = 0
        while (1):
            newseq = copy.deepcopy(seq)
            for i in range(n):
                newseq[perm[i]-1] = seq[i]
            seq = copy.deepcopy(newseq)
            t += 1
            if (seq == nseq):
                output_str = f'Length of {n}-premutator {perm} is: {t}\n'
                print(output_str)
                f.write(output_str)
                if (t > maxt):
                    maxt = t
                break

output_str = f'Maximum loop length: {maxt}\n'
print(output_str)
'''
import itertools
import copy

def get_permutations(nums):
    return list(itertools.permutations(nums))

seq = ['A','A','R','D','V','A','R','K','S']
seq2 = copy.deepcopy(seq)
n = len(seq)
nseq = []
for i in range(n):
    nseq.append(i+1)

permutations = get_permutations(nseq)
print('Got all permutations...')
cnt = 0

with open('output.txt', 'w') as f:
    for perm in permutations:
        print(perm)
        t = 0
        while (1):
            newseq = copy.deepcopy(seq)
            for i in range(n):
                newseq[perm[i]-1] = seq[i]
            seq = copy.deepcopy(newseq)
            t += 1
            if (seq == seq2):
                # output_str = f'Length of {n}-premutator {perm} is: {t}\n'
                # print(output_str)
                # f.write(output_str)
                if (t == 5):
                    output_str = f'Length of {n}-premutator {perm} is: {t}\n'
                    print(output_str)
                    f.write(output_str)
                    cnt += 1
                break

output_str = f'Loop length  = 4: {cnt}\n'
print(output_str)

