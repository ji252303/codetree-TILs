n = int(input())

table = []

for _ in range(n):
    table.append(list(map(int,input().split())))
 

def max_coins_in_3x3(table, n):
    max_coins = 0

    for i in range(n-2):
        for j in range(n-2):
            # 3x3 격자의 동전 개수를 계산.
            current_coins = 0
            for x in range(3):
                for y in range(3):
                    current_coins += table[i + x][j + y]
            
            max_coins = max(max_coins, current_coins)

    return max_coins

result = max_coins_in_3x3(table, n)
print(result)