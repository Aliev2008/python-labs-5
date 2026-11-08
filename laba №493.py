n, k = map(int, input().split())
row = ['I'] * n
for _ in range(k):
    m, h = map(int, input().split())
    for j in range(m - 1, h):
        row[j] = '.'
print(''.join(row))