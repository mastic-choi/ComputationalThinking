#변수를 선언한다.
sum_of_num = 0
number = 1
count = 0

#n이 0~100 사이의 값인지 확인
while  True :
    #데이터를 입력받는다.
    n = int(input(">> n = "))
    #echo checking
    print(">> 입력한 n = ", n)
    if 0 <= n <= 100:
        break
    else :
        print("\n>> 0 ~ 100 사이의 값을 입력하세요")

print("\n>> 0 ~ 100사이의 {N}의 배수 리스트 : " .format(N = n), end=" ")
while number <= 100:
    if number%n == 0:
        print(number, end = " ")
        sum_of_num = sum_of_num + number
        count = count + 1
    number = number + 1

print("\n\n>> 1 ~ 100 사이의 11의 배수의 수 : ",count)
print("   1 ~ 100 사이의 모든 11의 배수의 합 : ", sum_of_num)
