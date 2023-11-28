import math

def is_Prime_number(num): #소수 판별 알고리즘
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

#사용자로부터 숫자 입력받기
D =True
while D:
    inputNumber = int(input("1) 에라토스테니스의 체 알고리즘 통해 1부터 몇까지의 소수를 출력할까요? : "))
    print("2) 입력하신 숫자는 {}입니다.\n".format(inputNumber))
    if inputNumber <= 1:
        print("3) 1보다 큰 자연수를 입력해주세요.. :(")
    else:
        D = False
print("3) 에라토스테니스의 체 알고리즘 통해 1부터 {}까지의 소수를 출력합니다. \n".format(inputNumber))

#숫자리스트 생성
number_list = list(range(1, inputNumber+1))
result = number_list[:]

for i in range(inputNumber): #i에 list의 인덱스를 불러옵니다.
    if number_list[i] in result: #다음 원소가 result리스트에 있을때만 실행
        if number_list[i] == 1:
            result.remove(number_list[i])
        elif is_Prime_number(number_list[i]): #i가 소수일 때
            for k in range(number_list[i], inputNumber+1):
                if k in result:
                    if k%number_list[i]==0: #i의 배수 찾기
                        if k != number_list[i]:
                            result.remove(k)
print("\n4) 1부터 {}까지의 소수는 다음과 같습니다".format(inputNumber))
print(result)
print("\n5) 1부터 {}까지의 소수는 총 {}개입니다.".format(inputNumber, len(result)))
print("6) 감사합니다 :)")
