n, k = map(int,input().split())

command = []
blocks = [0] * (n + 1)

for _ in range(k):
    command.append(list(map(int,input().split())))

# 명령을 적용
for start, end in command:
    blocks[start - 1] += 1  # 시작점에 블럭을 더함
    if end < n:
        blocks[end] -= 1 

max_blocks = 0
current_blocks = 0

for i in range(n):
    current_blocks += blocks[i]
    if current_blocks > max_blocks:
        max_blocks = current_blocks

# 결과 출력
print(max_blocks)