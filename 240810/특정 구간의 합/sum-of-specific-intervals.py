n, m = map(int,input().split())

A = []
sum = []

A = list(map(int, input().split()))

def build__sum():
    global sum
    sum = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        sum[i] = sum[i - 1] + A[i - 1]

def range_sum(a1, a2):
     return sum[a2] - sum[a1 - 1]

build__sum()

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(range_sum(a1, a2))