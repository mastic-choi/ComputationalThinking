import time as t

D = True
#D = False

class Fibo:
    counter = 0
    memo = {}

    def fiboRecursive(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        else:
            return self.fiboRecursive(number - 1) + self.fiboRecursive(number - 2)
    
    def recursiveTimeTracker(self, x):
        self.start_time = t.time()
        self.exculated_fibo = self.fiboRecursive(x)
        self.end_time = t.time()
        self.elapsed_time = self.end_time - self.start_time
        if D:
            print("\nA-1) 제귀로 계산된 피보나치 수  : ", self.exculated_fibo)
            print("A-2) 제귀로 걸린 시간 : ", self.elapsed_time)
    
    def fiboLoof(self, number):
        a, b = 0 , 1
        for i in range(number):
            a , b = b, a + b
        return a
    
    def loofFiboTimeTracker(self, x):
        self.start_time = t.time()
        self.exculated_fibo = self.fiboLoof(x)
        self.end_time = t.time()
        self.elapsed_time = self.end_time - self.start_time
        if D:
            print("\nB-1) 루프로 계산된 피보나치 수  : ", self.exculated_fibo)
            print("B-2) 루프로 걸린 시간 : ", self.elapsed_time)





class Main:
    def main(self):
        x = int(input("1) n : "))
        if D:
            print("\n2) 입력하신 데이터는 "+str(x)+"입니다.")
        myFibo = Fibo()
        if D:
            print("\n instantation이 완료됐습니다.")
        myFibo.recursiveTimeTracker(x)
        myFibo.loofFiboTimeTracker(x)

#Main
m = Main()
m.main()