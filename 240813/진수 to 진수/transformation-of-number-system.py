a, b = map(int,input().split())

n = str(input())


change = int(n, a)


if b == 2:
    n_base_b = bin(change)[2:]  # '0b' 제거 후 b진수로 변환
elif b == 8:
    n_base_b = oct(change)[2:]  # '0o' 제거 후 b진수로 변환
elif b == 16:
    n_base_b = hex(change)[2:]  # '0x' 제거 후 b진수로 변환
else:
    n_base_b = str(change)  # b가 10이면 변환 없이 출력

    
print(n_base_b)