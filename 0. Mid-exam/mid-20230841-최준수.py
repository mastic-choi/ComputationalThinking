'''
선서 : 나는 양심에 따라 절대 부정행위를 하지 않겠습니다. 부정행위 적발 시 모든 민사, 형사상의 법적책임을 지겠습니다. 이름 최준수 (20230841), 2023년 10월 26일(목)
'''
import string #dexadecimal용
import math #GCD 계산용

def ishexadecimal(value): #수가 헥사데이말인지 확인하는 함수이다.
    for letter in value:
        if letter not in string.hexdigits:
            return False
    return True

in_list = []
D= True
i = 0
print(">> 5개의 값을 한 개씩 차례대로 입력하세요.")
while D:
    i = i +1
    usr_input = input("\n>> in_list에 추가할 {}번째 값을 입력하세요 : ".format(i))
    print(">>> 입력값(str type) : ",usr_input) #echo checking
    #입력 값이 숫자형(interger, floating-point, hexadecimal) 확인
    if usr_input.isnumeric() == True: #참이면 인티져
        numeric_input = int(usr_input)
        print(">>> 입력값 {S}가(이) integer {I}으(로) type-casting되었습니다" .format(S = usr_input, I = numeric_input))
        in_list.append(numeric_input)
    else :
        if ishexadecimal(usr_input) == True: #참이면 헥사 데시말
            hexa_input = int(usr_input, base = 16)
            print(">>> 입력값 {D}가(이) Decimal {I}(으)로 type-casting되었습니다" .format(D=usr_input, I = hexa_input))
            in_list.append(hexa_input)
        else :
            replaced_input = usr_input.replace('.','', 1)
            if replaced_input.isdigit() == True : #참이면 floating
                floating_input = float(usr_input)
                int_input = int(floating_input)
                print(">>> %.6f가(이) integer %d으로 type-casting되었습니다."%(floating_input, int_input))
                in_list.append(int_input)
        
            else : #String일 때 '추가할 값을 숫자형으로 다시 입력하세요' loop
                T = True
                while T:
                    print("\n>> WARING : 입력값이 숫자형(integer, flaoting-point, hexadecimal)이 아닙니다.")
                    usr_input = input("\n>> in_list에 추가할 {}번째 값을 숫자형으로 다시 입력하세요 : ".format(i))
                    print(">>> 입력값 : ",usr_input) #echo checking
                    if usr_input.isnumeric() == True: #참이면 인티져
                        numeric_input = int(usr_input)
                        print(">>> 입력값 {S}가(이) integer {I}으(로) type-casting되었습니다" .format(S = usr_input, I = numeric_input))
                        in_list.append(numeric_input)
                        T = False
                    else :
                        if ishexadecimal(usr_input) == True: #참이면 헥사 데시말
                            hexa_input = int(usr_input, base = 16)
                            print(">>> 입력값 {D}가(이) Decimal {I}(으)로 type-casting되었습니다" .format(D=usr_input, I = hexa_input))
                            in_list.append(hexa_input)
                            T = False
                        else :
                            replaced_input = usr_input.replace('.','', 1)
                            if replaced_input.isdigit() == True : #참이면 floating
                                floating_input = float(usr_input)
                                int_input = int(floating_input)
                                print(">>> %.6f가(이) integer %d으로 type-casting되었습니다."%(floating_input, int_input))
                                in_list.append(int_input)

    if i >= 5:
        D = False
print("\n>> in_list : ", in_list)
copyOfList = in_list[:] #deep copy
copyOfList.sort()
print("\n>> 오름차순 sort : ", copyOfList)

'''
문제 2번 진행
'''

#in_list에 입력된 값 중 제일 큰 수(large)와 제일 작은 수 (small)을 찾기
max_value_inList = max(in_list)
min_value_inList = min(in_list)

#최대값 최소값을 값으로 가지는 dic 생성
min_max = {}
min_max['min_key'] = min_value_inList
min_max['max_key'] = max_value_inList

print("\n>> min_max : ",min_max)

#GCD 계산후 dic에 추가
gcd = math.gcd(min_max["min_key"], min_max['max_key'])
print("\n>> 최대값 {MAX}와 최소값 {MIN}의 gcd : {G}".format(MAX = min_max['max_key'], MIN = min_max['min_key'], G = gcd))
min_max['gcd'] = gcd
print("\n>> min_max : ", min_max)
