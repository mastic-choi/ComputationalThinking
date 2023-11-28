import random
lotto_number = [] #빈 리스트 생성
while len(lotto_number) <6:
    x = random.randint(1,45) #1~45 사이의 무작위 숫자 생성
    if x not in lotto_number: #무작위 숫자가 이미 뽑힌적이 없는지 확인
        lotto_number.append(x) #lotto_number list에 집어 넣기
lotto_number.sort()    # 오름차순으로 정렬
print(lotto_number)