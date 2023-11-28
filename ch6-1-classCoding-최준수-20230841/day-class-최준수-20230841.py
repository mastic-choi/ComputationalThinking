import datetime

#D = False
D = True #디버깅 기법

class Calculate_date:

    stand_date = datetime.date(2023,1,1)
    wanna_date = 0
    weekdays = ['월', '화', '수', '목', '금', '토', '일']

    def usr_input(self):
        self.usr_input_date = input("\nA-1) 기준이 될 날짜를 입력해주세요(ex 2023.11.09) : ")
        if D:
            print("A-2) 사용자가 입력하신 기준일은 {}입니다.".format(self.usr_input_date))
        self.list_of_date = self.usr_input_date.split('.')
        self.stand_date = datetime.date(int(self.list_of_date[0]), int(self.list_of_date[1]), int(self.list_of_date[2]))

        self.wanna_date = int(input("\nA-3) 기준 일로부터 얼마 뒤의 날짜를 계산할까요? : "))
        if D:
            print("A-4) 사용자가 입력하신 값은 {}입니다.".format(self.wanna_date))
    
    def calculateDate(self):
        self.after_date = self.stand_date + datetime.timedelta(days = self.wanna_date)
        self.week_num = self.after_date.weekday()
        if D:
            print("\nB-1) {D}로부터 {C}일 후는 {A}입니다.".format(D = self.stand_date, C = self.wanna_date, A = self.after_date))
            print("B-2) {A}는 {W}요일 입니다.".format(A = self.after_date, W = self.weekdays[self.week_num]))


class Main:
    def main(self):
        if D:
            print("1) 프로그램을 실행합니다.")
        myDate = Calculate_date()
        if D:
            print("\n2) instantiation을 완료했습니다.")
            print("3)프로세스를 진행합니다.")
        myDate.usr_input()
        myDate.calculateDate()
        if D:
            print("\n4) 프로그램을 종료합니다.")

m = Main()
m.main()
