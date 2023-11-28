import time as t
import random

#사용자에게 숫자 받아오기
D = True
while D:
    num = int(input("1) 안녕하세요! 몇 개의 랜덤한 아이탬(1부터 100000)을 가진 리스트를 생성할까요? : "))
    if num < 1:
        print("\n2) 최소 한 개 이상의 숫자를 입력해 주세요.. :(")
    else :
        print("\n2) {}개의 랜덤한 아이탬을 가진 리스트를 생성합니다.".format(num))
        D = False

#랜덤한 숫자를 가진 리스트 생성하기
print("3) 랜덤하게 생성된 숫자들은 다음과 같습니다. : ", end = "")
num_list = [] # 빈 리스트 생성
for i in range(num):
    e = random.randint(1, 100000)
    num_list.append(e)
    print(e, end = " ")

#python 제공 sort 사용하기
pySort = num_list[:]
start_time_python = t.time()
pySort.sort()
end_time_python = t.time()
print("\n\n4) 파이썬 제공 sort기능으로 정렬한 리스트입니다. ", pySort)
print("5) 파이썬 제공 sort기능으로 정렬할때 걸린 시간은 {}입니다.".format(end_time_python-start_time_python, '.5f'))

#버블 정렬
bubblelist = num_list[:]
start_time_bubble = t.time()
length = len(bubblelist)-1
for i in range(length):
    for j in range(length-i):
        if bubblelist[j] > bubblelist[j+1]:
            bubblelist[j], bubblelist[j+1] = bubblelist[j+1], bubblelist[j] #둘의 위치 switch
end_time_bubble = t.time()
print("\n6) bubble sort 기능으로 정렬한 리스트입니다. ", bubblelist)
print("7) bubble sort 기능으로 정렬할때 걸린 시간은 {}입니다.".format(end_time_bubble-start_time_bubble, '.5f'))
print("8) 감사합니다 :)")