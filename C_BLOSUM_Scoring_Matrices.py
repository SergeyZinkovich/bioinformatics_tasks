import sys
from collections import Counter
import numpy as np
data = sys.stdin.readlines()

d = [Counter() for _ in range(len(data[0]) - 1)]
all_counter = Counter()

for i in range(len(data)):
    for j in range(len(data[0])-1):
        d[j][data[i][j]] += 1
        all_counter[data[i][j]] += 1

single_sum = sum(all_counter.values())
all_counter = sorted(all_counter.items())

obs = np.zeros((len(all_counter), len(all_counter)))
exp = np.zeros((len(all_counter), len(all_counter)))
ans = np.zeros((len(all_counter), len(all_counter)))

for i in range(len(all_counter)):
    for j in range(i+1):
        for k in range(len(data[0]) - 1):
            if i == j:
                tmp = d[k][all_counter[i][0]]
                obs[i][j] += tmp * (tmp - 1) / 2
            else:
                tmp1 = d[k][all_counter[i][0]]
                tmp2 = d[k][all_counter[j][0]]
                obs[i][j] += tmp1 * tmp2
        if i == j:
            exp[i][j] = (all_counter[i][1] / single_sum) ** 2
        else:
            exp[i][j] = (all_counter[i][1] / single_sum * all_counter[j][1] / single_sum) * 2
obs /= obs.sum()

ans = 2*np.log2(obs/exp)
ans[ans == -float('inf')] = 0

ans = np.round(ans)
ans = ans.astype(int)
for i in range(len(all_counter)):
    print(*ans[i][:i+1])
