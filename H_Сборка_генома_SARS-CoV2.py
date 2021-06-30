import numpy as np
from queue import Queue

data = open('input.txt', 'r').read().split()
data = [v for k, v in enumerate(data) if k % 2]

g = {}
g_r = {}
for s in data:
    for k in range(len(s)-30):
        if s[k+1:k+31] in g_r:
            g_r[s[k+1:k+31]].add(s[k:k+30])
        else:
            g_r[s[k+1:k+31]] = {s[k:k+30]}
        if s[k:k+30] in g:
            g[s[k:k+30]].add(s[k+1:k+31])
        else:
            g[s[k:k+30]] = {s[k+1:k+31]}

        if s[k+1:k+31] not in g:
            g[s[k+1:k+31]] = set()
        if s[k:k+30] not in g_r:
            g_r[s[k:k+30]] = set()


del data

b = False
for key, val in g_r.items():
    if len(val) % 2 != 1 and b:
        print('None')
        exit(0)
    if len(val) == 0 and not b:
        b = True
        start = key

if not b:
    start = key

del g_r

ans = start
st = Queue()
st.put(g[start].pop())
while st.qsize() > 0:
    cur = st.get()
    ans += cur[-1]
    if len(g[cur]) > 0:
        st.put(g[cur].pop())

print(ans)
