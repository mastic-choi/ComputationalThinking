import math
D = True
while D:
    k = int(input(">> 1~100사이의 자연수 중 조화급수를 계산할 항 k을 입력하세요 : "))
    print(">> 입력하신 자연수 k는 {K}입니다.".format(K=k))
    if 0<=k<=100:
        D = False
    else:
        print("\n>> 올바른 수를 입력하세요.")

sumOfLog = 0
for i in range(1, k+1):
    sumOfLog = sumOfLog+(1/i)
realSumOfLog = math.log(k+1)
errorRate = (realSumOfLog - sumOfLog) / realSumOfLog
print("\n>> 계산한 조화급수의 값은 {S}, 실제 값은 {R}입니다. 이 둘의 오차율은 {E}" . format(S=sumOfLog, R = realSumOfLog, E = errorRate))
