print()
year = int(input("> 연도를 입력하세요 >> "))

if(year % 400 == 0 )or((year%4 == 0) and (not(year%100 ==0))):
    print("\n%d is a leap year" %year)
else : 
    print("\n>>%d is not a leap year" %year)