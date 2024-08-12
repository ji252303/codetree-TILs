from datetime import datetime, timedelta

m1,d1,m2,d2 = map(int,input().split())
A = str(input())

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

start_day_index = weekdays.index("Mon")

# 시작 날짜와 종료 날짜를 datetime 객체로 생성
start_date = datetime(2024, m1, d1)
end_date = datetime(2024, m2, d2)

target_day_index = weekdays.index(A)
current_day_index = start_day_index

days_to_target = (target_day_index - current_day_index) % 7
target_date = start_date + timedelta(days=days_to_target)

# target_date가 start_date보다 작으면, 다음 주의 해당 요일로 설정
if target_date < start_date:
    target_date += timedelta(days=7)

# 해당 요일이 몇 번 등장하는지 세기
count = 0
while target_date <= end_date:
    count += 1
    target_date += timedelta(days=7)

print(count)