D = True
# 올바른 월, 일인지 확인
while D:
    y = int(input(">> 요일을 계산할 날짜의 년도를 입력해 주세요. : "))
    m = int(input(">> 요일을 계산할 날짜의 월을 입력해 주세요. : "))
    d = int(input(">> 요일을 계산할 날짜의 일을 입력해 주세요 : "))
    
    # 입력 확인
    print("당신이 입력하신 날짜는 {}년 {}월 {}일입니다.".format(y, m, d))
    
    if y > 0 and 1 <= m <= 12 and 1 <= d <= 31:
        D = False
    else:
        print("정확한 날짜를 입력해주세요.")

# 1년 1월 1일로부터 얼마나 지났는지 확인
n = 0
n = n + (y - 1) * 365
n = n + (y - 1) // 4

days_elapsed = 0

# 1월부터 입력한 월 이전까지의 일 수 계산
for month in range(1, m):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days_elapsed = days_elapsed + 31
    elif month in [4, 6, 9, 11]:
        days_elapsed = days_elapsed + 30
    elif month == 2:
        # 윤년인지 아닌지 확인하여 2월의 일 수 계산
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            days_elapsed = days_elapsed + 29  # 윤년
        else:
            days_elapsed = days_elapsed + 28

n = n + days_elapsed + d - 1

# 결과 출력
print("입력하신 {Y}년 {M}월 {D}일은 1년 1월 1일로부터 {N}일이 지났습니다.".format(Y=y, M=m, D=d, N=n))

# 요일 계산
Day_of_the_week = ["월", "화", "수", "목", "금", "토", "일"]
toDayWeek = Day_of_the_week[n % 7]

print("입력하신 {Y}년 {M}월 {D}일은 {W}요일 입니다.".format(Y=y, M=m, D=d, W=toDayWeek))