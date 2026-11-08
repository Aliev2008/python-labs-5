import sys

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    sign = '-' if s[0] == '-' else ''
    d = s.lstrip('-')
    print(max(int(sign + (d[:i] + d[i + 1:] or '0')) for i in range(len(d))))