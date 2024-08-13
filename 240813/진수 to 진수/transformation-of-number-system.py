a, b = map(int,input().split())

n = str(input())


if a in [2, 8]:
    change = int(n, a)

    result = format(change, 'b')  # b진수로 변환하여 문자열로 출력

    # 결과 출력
    print(result)