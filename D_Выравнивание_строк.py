d, e = map(int, input().split())

a = input()
a = {val: i for i, val in enumerate(a)}

r = [list(map(int, input().split())) for _ in range(len(a))]

s1 = input()
s2 = input()

m = [[0 for __ in range(len(s2)+1)] for _ in range(len(s1)+1)]
x = [[0 for __ in range(len(s2)+1)] for _ in range(len(s1)+1)]
y = [[0 for __ in range(len(s2)+1)] for _ in range(len(s1)+1)]
hist_m = [[0 for __ in range(len(s2)+1)] for _ in range(len(s1)+1)]
hist_x = [[0 for __ in range(len(s2)+1)] for _ in range(len(s1)+1)]
hist_y = [[0 for __ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    x[i][0] = -10000
    # hist[i][0] = 1

for j in range(1, len(s2)+1):
    x[0][j] = d + (j-1) * e
    hist_x[0][j] = 1

for j in range(1, len(s2)+1):
    m[0][j] = -10000

for i in range(1, len(s1)+1):
    m[i][0] = -10000

m[0][0] = 0

for j in range(1, len(s2)+1):
    y[0][j] = -10000

for i in range(1, len(s1)+1):
    y[i][0] = d + (i-1) * e
    hist_y[i][0] = -1


# dd[0][0] = r[a[s1[0]]][a[s2[0]]]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2) + 1):
        if m[i-1][j-1] >= x[i-1][j-1] and m[i-1][j-1] > y[i-1][j-1]:
            m[i][j] = r[a[s1[i - 1]]][a[s2[j - 1]]] + m[i-1][j-1]
            hist_m[i][j] = 0
        elif x[i-1][j-1] > m[i-1][j-1] and x[i-1][j-1] > y[i-1][j-1]:
            m[i][j] = r[a[s1[i - 1]]][a[s2[j - 1]]] + x[i-1][j-1]
            hist_m[i][j] = 1
        else:
            m[i][j] = r[a[s1[i - 1]]][a[s2[j - 1]]] + y[i-1][j-1]
            hist_m[i][j] = -1

        if m[i][j-1] + d >= x[i][j-1] + e and m[i][j-1] + d >= y[i][j-1] + d:
            x[i][j] = m[i][j-1] + d
            hist_x[i][j] = 0
        elif y[i][j-1] + d >= x[i][j-1] + e and y[i][j-1] + d >= m[i][j-1] + d:
            x[i][j] = y[i][j-1] + d
            hist_x[i][j] = -1
        else:
            x[i][j] = x[i][j-1] + e
            hist_x[i][j] = 1

        if m[i-1][j] + d >= y[i-1][j] + e and m[i-1][j] + d >= x[i-1][j] + d:
            y[i][j] = m[i-1][j] + d
            hist_y[i][j] = 0
        elif x[i-1][j] + d > y[i-1][j] + e and x[i-1][j] + d >= m[i-1][j] + d:
            y[i][j] = x[i-1][j] + d
            hist_y[i][j] = 1
        else:
            y[i][j] = y[i-1][j] + e
            hist_y[i][j] = -1


i = len(s1)
j = len(s2)
if x[-1][-1] >= y[-1][-1] and x[-1][-1] >= m[-1][-1]:
    ptr = 1
elif y[-1][-1] >= x[-1][-1] and y[-1][-1] >= m[-1][-1]:
    ptr = -1
else:
    ptr = 0
ans1, ans2 = [], []
while i != 0 or j != 0:
    if ptr == 0:
        ans1.append(s1[i-1])
        ans2.append(s2[j-1])
        ptr = hist_m[i][j]
        i -= 1
        j -= 1
    elif ptr == 1:
        ans2.append(s2[j-1])
        ans1.append('-')
        ptr = hist_x[i][j]
        j -= 1
    else:
        ans2.append('-')
        ans1.append(s1[i-1])
        ptr = hist_y[i][j]
        i -= 1


print(max(m[-1][-1], x[-1][-1], y[-1][-1]))
ans1.reverse()
ans2.reverse()
print(''.join(ans1))
print(''.join(ans2))