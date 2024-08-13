n = int(input())

line = []

for _ in range(n):
    line.append(list(map(int,input().split())))

events = []

for start, end in line:
    events.append((start, 'start'))
    events.append((end, 'end'))

events.sort(key=lambda x: (x[0], x[1] == 'start'))

max_point = 0
current = 0

for event in events:
    if event[1] == 'start':
        current += 1
        max_point = max(max_point, current)
    else:
        current -= 1

# 결과 출력
print(max_point)