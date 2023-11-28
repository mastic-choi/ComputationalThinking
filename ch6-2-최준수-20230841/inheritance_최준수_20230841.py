from abc import ABC
import datetime, time, turtle

#D = False
D = True

class Metaclass(ABC): #추상 메소드
    pass

class Day_class(Metaclass):
        weekdays = ['월', '화', '수', '목', '금', '토', '일']
        
        def __init__(self, stand_date = "2000.01.01", wanna_date = 0):
            self.__stand_date = datetime.date(int(stand_date.split('.')[0]), int(stand_date.split('.')[1]), int(stand_date.split('.')[2]))
            self.__wanna_date = wanna_date
            
        def getStandDate(self): #private변수를 출력하는 코드
            return self.__stand_date
        
        def setStandDate(self, stand_date): #private변수를 입력받는 코드
            self.__stand_date = datetime.date(int(stand_date.split('.')[0]), int(stand_date.split('.')[1]), int(stand_date.split('.')[2]))
            if D:
                print("dcs) self.__stand_date = ", self.__stand_date)

        def getWannaDate(self): #private변수를 출력하는 코드
            return self.__wanna_date
        
        def setWannaDate(self, wanna_date): #private변수를 입력받는 코드
            self.__wanna_date = wanna_date
            if D:
                print("dcs) self.__wanna_date = ", self.__wanna_date)
        def calculateDate(self): #요일을 계산하는 코드
            self.after_date = self.__stand_date + datetime.timedelta(days = self.__wanna_date)
            if D:
                print("\nd-1) {D}로부터 {C}일 후는 {A}입니다.".format(D = self.__stand_date, C = self.__wanna_date, A = self.after_date))
                print("d-2) {A}는 {W}요일 입니다.".format(A = self.after_date, W = self.weekdays[self.after_date.weekday()]))

class Fibo_class(Metaclass):
    def __init__(self, number = 0):
        self.__number = number
    
    def getNumber(self):
        return self.__number
    
    def setNumber(self, usr_input_number):
        self.__number = usr_input_number
        if D:
            print("fcs) self.__number = ", self.__number)
    
    def fiboRecursive(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        else :
            return self.fiboRecursive(x - 1) + self.fiboRecursive(x - 2)
    
    def fiboLoof(self, x):
        a, b = 0 , 1
        for i in range(x):
            a , b = b, a + b
        return a
    
    def processFibo(self):
        self.start_time = time.time()
        self.exculated_fibo = self.fiboRecursive(self.__number)
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        if D:
            print("\nf-1) 제귀로 계산된 피보나치 수  : ", self.exculated_fibo)
            print("f-2) 제귀로 걸린 시간 : ", self.elapsed_time)
        self.start_time = time.time()
        self.exculated_fibo = self.fiboLoof(self.__number)
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        if D:
            print("\nf-3) 루프로 계산된 피보나치 수  : ", self.exculated_fibo)
            print("f-4) 루프로 걸린 시간 : ", self.elapsed_time)

class Tree_class(Metaclass):
    def __init__(self):
        self.s = turtle.Screen()
        self.t = turtle.Turtle()
        self.angle = 30

    def drawTree(self, line_length):
        if line_length > 0:
            self.t.forward(line_length)
            self.t.left(self.angle)
            self.drawTree(line_length - 10)

            self.t.right(self.angle)
            self.t.right(self.angle)
            self.drawTree(line_length - 10)

            self.t.left(self.angle)
            self.t.backward(line_length)

class Hanoi_class(Metaclass):
    def __init__(self, number = 0, moveFrom = "A", moveTemp = "B", moveTo = "C"):
        self.number = number
        self.moveFrom = moveFrom
        self.moveTemp = moveTemp
        self.moveTo = moveTo
    
    def setNumber(self, x):
        self.number = x
        print("hcs) self.number = ", self.number)

    def move(self, number):
        if number == 1:
            return 1
        else:
            return 1 + 2*self.move(number - 1)
    
    def hanoi(self, n, moveFrom, moveTemp, moveTo):
        if n == 1:
            if D:
                print("{N}을 {F}에서 {T}으로 이동".format(N = n, F=moveFrom, T = moveTo))
            return 
        else :
            self.hanoi(n-1,moveFrom,moveTo,moveTemp)
            if D:
                print("{N}을 {F}에서 {T}으로 이동".format(N = n, F = moveFrom, T = moveTo))
            self.hanoi(n-1,moveTemp,moveFrom,moveTo)
            if D:
                print("{N}을 {T}에서 {F}으로 이동".format(N = n, T = moveTemp, F = moveFrom))  
    
    def processHanoi(self):
        if D:
            print("\nh-1) 하노이의 탑을 몇번 움직어야 하는지 계산합니다. ")
        self.count_of_move = self.move(self.number)
        if D:
            print("h-2) 원반 개수가 {N}개 일 때, {C}번 원반을 옮겨야 합니다.".format(N=self.number, C = self.count_of_move))
            print("\nh-3) 원반이동 process를 출력합니다.")
        self.hanoi(self.number, self.moveFrom, self.moveTemp, self.moveTo)

class Main:
    
    def day(self):
        myDay = Day_class()
        if D:
            print("\nmainD-1) Day_class의 instantiation을 완료했습니다.")
        self.usr_input_date = input("\nm-2) 기준이 될 날짜를 입력해주세요(ex 2023.11.09) : ")
        if D:
            print("\nmainD-3) 사용자가 입력하신 기준일은 {}입니다.".format(self.usr_input_date))
            print("mainD-4) Class의 Setter를 통해 attribute 변경 시도.")
        myDay.setStandDate(self.usr_input_date)
        if D:
            print("\nmainD-5) Day_class의 standardDate : ", myDay.getStandDate())
        self.usr_wanna_date = int(input("\nm-6) 기준 일로부터 얼마 뒤의 날짜를 계산할까요? : "))
        myDay.setWannaDate(self.usr_wanna_date)
        if D:
            print("mainD-6) Day_class의 wannaDate : ", myDay.getWannaDate())
        myDay.calculateDate()    
    
    def fibo(self):
        myFibo = Fibo_class()
        if D :
            print("\nmainF-1) Fibo_class의 instantiation을 완료했습니다.")
        self.usr_input_number = int(input("mainF-2) Fibo 계산하고 싶은 수를 입력하세요 : "))
        if D:
            print("\nmainF-3) {}를 입력하셨습니다".format(self.usr_input_number))
            print("mainF-4) Class의 Setter를 통해 attribute 변경 시도")
        myFibo.setNumber(self.usr_input_number)
        if D:
            print("\nmainF-5) Fibo_class의 Number : ", myFibo.getNumber())
        myFibo.processFibo()   
    
    def tree(self):
        myTree = Tree_class()
        if D:
            print("\nmainT-1) Tree_class의 instantiation을 완료했습니다.")
        self.usr_input_length = int(input("mainT-2) 나무의 초기 굵기를 몇으로 설정하시겠습니까? : "))
        if D:
            print("\nmainT-3) {}를 입력하셨습니다".format(self.usr_input_length))
        myTree.drawTree(self.usr_input_length)
    
    def hanoi(self):
        myHanoi = Hanoi_class()
        if D:
            print("\nmainH-1) Hanoi_class의 instantiation을 완료했습니다.")
        self.usr_number = int(input("mainH-2) 원반 개수가 몇인 하노이탑을 연산할까요? : "))
        if D:
            print("\nmainH-3) {}를 입력하셨습니다".format(self.usr_number))
        myHanoi.setNumber(self.usr_number)
        myHanoi.processHanoi()


#Main
m = Main()
m.day()
m.fibo()
m.tree()
m.hanoi()