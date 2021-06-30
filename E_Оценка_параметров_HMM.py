import sys
from collections import Counter
import numpy as np

types = ['A-', 'C-', 'G-', 'T-', 'A+', 'C+', 'G+', 'T+']
pairs_freq = {i: {j: 0 for j in types} for i in types}
single_neg_freq = {i[0]: 0 for i in types[:4]}

f = open('input.txt')

data = f.readlines()

line = data[-1][:-1]
islands = data[:-1]

positive = np.zeros((len(line)), dtype=bool)

for island in islands:
    b, e = map(int, island.split())
    for i in range(b-1, e):
        positive[i] = True

for i in range(len(line)-1):
    if not positive[i]:
        single_neg_freq[line[i]] += 1

    key1 = line[i] + ('+' if positive[i] else '-')
    key2 = line[i + 1] + ('+' if positive[i + 1] else '-')

    pairs_freq[key1][key2] += 1

if not positive[-1]:
    single_neg_freq[line[-1]] += 1

sum_single_neg_freq = sum(single_neg_freq.values())
sum_pairs_freq = {key: sum(val.values()) for key, val in pairs_freq.items()}

fw = open('output.txt', 'w')

for i in single_neg_freq.values():
    print(np.round(np.log((i + 10e-31) / (sum_single_neg_freq + 1)), decimals=5), file=fw)


for key, val in pairs_freq.items():
    for i in val.values():
        print(np.round(np.log((i + 10e-31) / (sum_pairs_freq[key] + 1)), decimals=5), file=fw)


