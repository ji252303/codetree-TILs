a,b = map(int,input().split())

small = min(a,b)
big = max(a,b)

def re(a,b):
    result1 = small + 10
    result2 = big * 2

    return result1, result2

result = re(a,b)
print(f"{result[0]} {result[1]}")