import math

n = int(input())

li = []

li = list(map(int,input().split()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def re_lcm(n, idx = 0):
    if idx == len(n) - 1:
        return n[idx]
    return lcm(n[idx], re_lcm(n,idx+1))

result = re_lcm(li)
print(result)