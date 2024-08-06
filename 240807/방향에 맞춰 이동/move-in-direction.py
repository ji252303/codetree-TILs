n = int(input())

moves = []


for _ in range(n):
    direction, distance = input().split()
    moves.append((direction, int(distance)))

def move_position(n, moves):
    x, y = 0, 0

    direction_map = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    # 이동 명령어 처리
    for direction, distance in moves:
        dir_num = direction_map[direction]
        for _ in range(distance):
            x += dx[dir_num]
            y += dy[dir_num]

    return x, y

r_x, r_y = move_position(n, moves)
print(r_x, r_y)