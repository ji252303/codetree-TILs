from datetime import datetime

n = int(input())

data = []

def find_rain():

    for _ in range(n):
        date_str, day, weather = input().split()  
        date = datetime.strptime(date_str, "%Y-%m-%d")  # 문자열을 날짜로 변환
        data.append((date, day, weather)) 

    data.sort(key=lambda x: x[0])

    for date, day, weather in data:
        if weather == "Rain":
            print(f"{date.strftime('%Y-%m-%d')} {day} {weather}")
            return


find_rain()