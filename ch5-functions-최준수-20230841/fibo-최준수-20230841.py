import time as t

counter = 0
memo = {}

def fibobyrecursive(n):
    if n == 0 : 
        return 0
    if n == 1:
        return 1
    else :
        return fibobyrecursive(n-1)+fibobyrecursive(n-2)

def recursive(x):      
    start_time = t.time()
    exculated_fibo = fibobyrecursive(x)
    end_time = t.time()
    global recursive_time
    recursive_time = end_time-start_time
    print("\n>> 제귀로 계산된 피보나치 수  : ", exculated_fibo)
    print(">> 제귀로 걸린 시간 : ", recursive_time)

def fibobyLoof(x):
    a, b = 0, 1
    for i in range(x):
        a, b = b, a + b
    return a

def loof(n):
    start_time = t.time()
    exculated_fibo = fibobyLoof(n)
    end_time = t.time()
    global loof_time
    loof_time = end_time-start_time
    print("\n>> 루프로 계산된 피보나치 수  : ", exculated_fibo)
    print(">> 루프로 걸린 시간 : ", loof_time)

def memo_fibo(n):
    global counter
    counter = counter + 1
    if n in memo:
        print("\nf1) memo[{}] = {} 값 사용".format(n, memo[n]))
        return memo[n]
    if n == 0:
        memo[n] = 0
        print("f2) memo[{}] = {} 저장".format(n, memo[n]))
    elif n == 1:
        memo[n] = 1
        print("f3) memo[{}] = {} 저장".format(n, memo[n]))
    else:
        memo[n] = memo_fibo(n-1) + memo_fibo(n-2)
        print("f4) memo[{}] = {} 저장".format(n, memo[n]))
    return memo[n]

def fibowithMemory(n):
    start_time = t.time()
    exculated_fibo_memo = memo_fibo(n)
    end_time = t.time()
    global recursive_time_memo
    recursive_time_memo = end_time-start_time
    print("\n>> 제귀로 계산된 피보나치 수(Memo)  : ", exculated_fibo_memo)
    print(">> 제귀로 걸린 시간(Memo) : ", recursive_time_memo)

def main():
    x = int(input(">> n : "))
    print(">> 입력하신 데이터는 "+str(x)+"입니다.")
    recursive(x)
    loof(x)
    fibowithMemory(x)
    if loof_time > recursive_time and recursive_time < recursive_time_memo:
        print("\n>> 피보나치를 제귀로 계산하는 것이 가장 유리합니다.")
    elif loof_time < recursive_time and loof_time < recursive_time_memo:
        print("\n>> 피보나치를 루프로 계산하는 것이 가장 유리합니다.")
    elif recursive_time_memo < loof_time and recursive_time > recursive_time_memo:
        print("\n>> 피보나치를 메모리가 존재하는 재귀함수로 계산하는 것이 가장 유리합니다.")


#main()
if __name__ == "__main__":
    main()