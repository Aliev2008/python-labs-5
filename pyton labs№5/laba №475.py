import sys

for line in sys.stdin:
    a = list(map(int, line.split()))
    result = sorted(x for x in set(a) if a.count(x) > 1)
    if result:
        print(*result)