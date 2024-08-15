n = int(input())

commands = []

for _ in range(n):
    commands.append(list(input().split()))

def flip_tiles(commands):
    # 타일의 색상 정보를 저장할 딕셔너리
    tiles = {}
    
    
    current_position = 0
    
    for command in commands:
        x, direction = command.split()
        x = int(x)
        
        if direction == 'L':
            for i in range(current_position, current_position - x, -1):
                if i not in tiles:
                    tiles[i] = 'W'  # 기본적으로 왼쪽으로 뒤집으면 흰색으로
                elif tiles[i] == 'G':
                    tiles[i] = 'W'
                elif tiles[i] == 'W':
                    tiles[i] = 'G'
                elif tiles[i] == 'B':
                    tiles[i] = 'W'
            current_position -= (x - 1)  # 마지막에 위치한 타일로 이동
        elif direction == 'R':
            for i in range(current_position, current_position + x):
                if i not in tiles:
                    tiles[i] = 'B'  # 기본적으로 오른쪽으로 뒤집으면 검은색으로
                elif tiles[i] == 'G':
                    tiles[i] = 'B'
                elif tiles[i] == 'W':
                    tiles[i] = 'B'
                elif tiles[i] == 'B':
                    tiles[i] = 'G'
            current_position += (x - 1)  # 마지막에 위치한 타일로 이동
    
    # 결과 계산
    white_count = sum(1 for color in tiles.values() if color == 'W')
    black_count = sum(1 for color in tiles.values() if color == 'B')
    
    return white_count, black_count

# 입력 명령
commands = ["4 R", "5 L", "7 R", "4 L"]
white_count, black_count = flip_tiles(commands)
print(white_count, black_count)