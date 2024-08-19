n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

def max_same_length(arr):
    max_length = 1  
    current_length = 1

    for i in range(1, len(arr)):
        # 현재 수와 이전 수의 부호 비교
        if (arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0):
            current_length += 1  # 부호가 같으면 길이 증가
        else:
            max_length = max(max_length, current_length) 
            current_length = 1  

    max_length = max(max_length, current_length)
    
    return max_length

print(max_same_length(arr))