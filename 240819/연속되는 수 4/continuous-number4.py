n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

def max_increasing_length(arr):
    if not arr:  
        return 0

    max_length = 1  
    current_length = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:  # 현재 숫자가 이전 숫자보다 크면
            current_length += 1  # 현재 길이를 증가
        else:
            max_length = max(max_length, current_length) 
            current_length = 1 

    max_length = max(max_length, current_length)  
    
    return max_length


print(max_increasing_length(arr))