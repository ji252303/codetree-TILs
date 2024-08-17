n = int(input())

num = []

for _ in range(n):
    num.append(int(input()))

def max_result(num):
    if not num:  
        return 0

    max_count = 1
    current_count = 1

    for i in range(1, len(num)):
        if num[i] == num[i - 1]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1

    return max_count

print(max_result(num))