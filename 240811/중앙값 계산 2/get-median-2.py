n = int(input())

A = []

A = list(map(int,input().split()))

def print_medians(A):
    data = []
    
    for i in range(len(A)):
        data.append(A[i])
        # 홀수 번째 원소일 때
        if (i + 1) % 2 != 0:
            mid_li = []
            data.sort()  # 리스트를 정렬
            mid = data[len(data) // 2]  # 중앙값 계산
            print(mid, end=' ')  # 중앙값 출력

print_medians(A)