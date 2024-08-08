a,b = map(int,input().split())



def re(a,b):
    if a < b:
        a = a+10
        b = b*2
    else:
        a = a * 2
        b = b + 10

    return a, b

result = re(a,b)
print(f"{result[0]} {result[1]}")