import datetime

def usr_input():
    usr_input_date = input("A-1) 기준이 될 날짜를 입력해주세요(ex 2023.11.09) : ")
    print("A-2) 사용자가 입력하신 기준일은 {}입니다.".format(usr_input_date))
    list_of_date = usr_input_date.split('.')
    type_casted_date = datetime.date(int(list_of_date[0]), int(list_of_date[1]), int(list_of_date[2]))

    wanna_calcu_date = int(input("\nA-3) 기준 일로부터 얼마 뒤의 날짜를 계산할까요? : "))
    print("A-4) 사용자가 입력하신 값은 {}입니다.".format(wanna_calcu_date))
    return type_casted_date, wanna_calcu_date

def calculate_date(date, calcu_date):
    after_date = date + datetime.timedelta(days=calcu_date)
    print("\nB-1) {D}로부터 {C}일 후는 {A}입니다.".format(D = date, C = calcu_date, A = after_date))
    week_num = after_date.weekday()
    weekdays = ['월', '화', '수', '목', '금', '토', '일']
    print("B-2) {A}는 {W}요일 입니다.".format(A = after_date, W = weekdays[week_num]))
    return after_date, weekdays[week_num]

if __name__ == "__main__":
    input_date, calcu = usr_input()
    calculate_date(input_date, calcu)

