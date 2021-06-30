types = ['A-', 'C-', 'G-', 'T-', 'A+', 'C+', 'G+', 'T+']
pairs_freq = {i: {j: 0 for j in types} for i in types}
single_freq = {i: 0 for i in types}
del types

f = open('input.txt')
line = f.readlines()
f.close()
del f

for i in range(8):
    key, val = line[i].split()
    single_freq[key] = float(val)

for i in range(8, len(line) - 1):
    key1, key2, val = line[i].split()
    pairs_freq[key1][key2] = float(val)

line = line[-1].split()[0]

p = [[0 for _ in range(len(line))] for __ in range(2)]

d = [0, 0]
d[0] = single_freq[line[0] + '-']
d[1] = single_freq[line[0] + '+']

d_prev = [0, 0]
k1, k2 = 0, 0

for i in range(1, len(line)):
    d_prev = d[:]
    k1 = d_prev[0] + pairs_freq[line[i - 1] + '-'][line[i] + '-']
    k2 = d_prev[1] + pairs_freq[line[i - 1] + '+'][line[i] + '-']
    if k1 > k2:
        d[0] = k1
    else:
        d[0] = k2
        p[0][i] = 1

    k1 = d_prev[0] + pairs_freq[line[i - 1] + '-'][line[i] + '+']
    k2 = d_prev[1] + pairs_freq[line[i - 1] + '+'][line[i] + '+']
    if k1 > k2:
        d[1] = k1
    else:
        d[1] = k2
        p[1][i] = 1

del line
del single_freq
del pairs_freq

ans = []

ptr = 0 if d[0] > d[1] else 1

if ptr == 1:
    ans.append(len(p[0]))

for i in range(len(p[0]) - 1, 0, -1):
    if ptr != p[ptr][i]:
        if ptr == 1:
            ans.append(i + 1)
        else:
            ans.append(i)
        ptr = p[ptr][i]

if ptr == 1 and len(ans) % 2 != 0:
    ans.append(1)

ans.reverse()

fw = open('output.txt', 'w')

for i in range(len(ans) // 2):
    print(ans[i * 2], ans[i * 2 + 1], file=fw)
