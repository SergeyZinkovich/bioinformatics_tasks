import numpy as np
from queue import Queue

s = open('input.txt', 'r').read().split()[0]
ans = ['.' for _ in range(len(s))]
count = 0
f = np.zeros((len(s), len(s)))


def sss(a, b):
    pairs = [
        ['A', 'U'],
        ['G', 'C'],
        # ['G', 'U'],
        ['U', 'A'],
        ['C', 'G'],
        # ['U', 'G'],
        # ['A', 'T'],
        # ['T', 'A'],
    ]
    if [a, b] in pairs:
        return 1
    else:
        return 0


for t in range(4, len(s)):
    for i in range(len(s) - t):
        j = i + t

        m = 0
        for k in range(i+1, j-2):
            m = max(m, f[i][k] + f[k+3][j])

        f[i][j] = max(f[i+1][j-1] + sss(s[i], s[j]), m, f[i+1][j], f[i][j-1])

q = Queue()
q.put((0, len(s)-1))
while q.qsize() > 0:
    i, j = q.get()

    if i >= j:
        continue

    if f[i+1][j] == f[i][j]:
        q.put((i+1, j))
    elif f[i][j-1] == f[i][j]:
        q.put((i, j-1))
    elif f[i+1][j-1] + sss(s[i], s[j]) == f[i][j]:
        ans[i] = '>'
        ans[j] = '<'
        count += 1
        q.put((i+1, j-1))
    else:
        for k in range(i+1, j):
            if f[i][k] + f[k+1][j] == f[i][j]:
                q.put((k+1, j))
                q.put((i, k))
                break

print(count, ''.join(ans), file=open('output.txt', 'w'))




