numbers = list(map(float, input().split()))
count = 0
for x in numbers:
    if x > 0:
        count += 1
print(count)