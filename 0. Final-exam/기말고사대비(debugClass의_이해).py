"""
BankAccount라는 예제를 통해 debugClass을 이해해 봅시다.
"""
class BankAccount:
    """
    Super Class
    """
    def __init__(self, in_name : str, in_number : int, in_balanace : int):
        if D :
            print("\nba_i) name = {N}".format(N = in_name))
            print("ba_i) number = {N}".format(N = in_number))
            print("ba_i) name = {B}".format(B = in_balanace))

        self.balance = in_balanace
        self.name = in_name
        self.number = in_number

    def withdraw(self, in_amount : int):
        """
        usr의 BankAccount의 있는 값을 인출하는 함수
        """
        if D:
            print("\nw-1) 현재 게좌 금액 : {}".format(self.balance))
            print("w-2) 찾는 금액의 amount : {}".format(in_amount))

        self.balance -= in_amount
        if D:
            print("w-3) 인출 후 사용자 계좌 금액 : {}".format(self.balance))
        return self.balance
    
    def deposit(self, in_amount : int):
        """
        usr의 BankAccount의 있는 값을 입금하는 함수
        """
        if D:
            print("\nd-1) 현재 게좌 금액 : {}".format(self.balance))
            print("\nd-2) in_amount : {}".format(in_amount))
        self.balance += in_amount
        if D :
            print("\nd-3) 입금 후 게좌 금액 : {}".format(self.balance))
        return self.balance

class savingsAccount(BankAccount):
    """
    Super Class인 BankAccount의 ChildClass 
    in_name : 예금주 이름, 
    in_number : 계좌번호, 
    in_balance : 계좌 금액, 
    in_interset_rate : 이자율
    """
    def __init__(self, in_name, in_number, in_balance, in_interset_rate):
        if D:
            print("\nsa_i) name = {}".format(in_name))
            print("sa_i) number = {}".format(in_number))
            print("sa_i) balance = {}".format(in_balance))
            print("sa_i) interest_rate = {}".format(in_interset_rate))

        super().__init__(in_name, in_number, in_balance) #부모클래스(BankAccount)에 집근
        self.__interest_rate = in_interset_rate #private 변수로 선언

    def set_interest_rate(self, in_interset_rate):
        self.__interest_rate = in_interset_rate #private 변수로 선언
        if D:
            print("set_int) self.__interest_rate = {}".format(self.__interest_rate))
    
    def get_interest_rate(self):
        if D:
            print("get_int) self.__interest_rate = {}".format(self.__interest_rate))
        return self.__interest_rate
    
    def add_interest(self):
        """
        예금이자를 받는 기능을 구현했다.
        """
        self.balance += self.balance*self.__interest_rate
        if D:
            print("add_int) self.balance = {}".format(self.balance))

class checkingAccount(BankAccount):
    """
    수표를 발행 하는 클래스이다.
    """
    def __init__(self, in_name: str, in_number: int, in_balanace: int):
        if D:
            print("\ncai_1) name = {}, number = {}, balance = {}".format(in_name, in_number, in_balanace))       
        super().__init__(in_name, in_number, in_balanace)

        self.withdraw_charge = 10000
        if D:
            print("\ncai_2) 수표 발행 수수료 = {}".format(self.withdraw_charge))
    def withdraw(self, in_amount):
        if D:
            print("\ncaw) amount = {}".format(in_amount))
        return BankAccount.withdraw(self, in_amount + self.withdraw_charge)
    def deposit(self, in_amount: int):
        if D:
            print("\ncade) amount = {}".format(in_amount))
        return BankAccount.deposit(self, in_amount)
    
class Debugging_option:
    """
    입력 값을 받아서 디버깅을 원하면 D = False로 변경하는 함수
    """
    def __init__(self, option):
        self.debug_option = option
    
    def in_option(self):
        #debugging option : default - >> bank "N"
        self.debug_option = input("\n>>> Debugging을 원하시나요? : (Y or N) : ")
        return self.debug_option
    

#main
if __name__ == "__main__":
    debug = Debugging_option("N")

    deb_option = debug.in_option()

    if deb_option in ["Y", 'y', 'yes', 'Yes', 'YES']:
        D = True
        print("1) deb_option = ", deb_option)
    else :
        D = False

    if D:
        print("2) SavingsAccount class의 객체 생성")
    saving_acc = savingsAccount("김국민", 2050110, 10000, 0.05)

    saving_acc.get_interest_rate()
    saving_acc.add_interest()
    print("3) 저축예금의 잔액 = ",saving_acc.balance)

    if D:
        print("\n4) SavingAccount 금리 변경 인하 : 0.05 ---> 0.03")
    saving_acc.set_interest_rate(0.03)
    saving_acc.get_interest_rate()
    saving_acc.add_interest()
    print("5) 저축예금의 잔액 = ", saving_acc.balance)

    if D:
        print("\n6) CheckingAccount class의 객체 생성")
    checking_acc =checkingAccount("박소프", 2040200, 2000000)
    checking_acc.withdraw(100000)
    checking_acc.deposit(200000)

    print("\n 7) 당좌예금의 잔액 = ", checking_acc.balance)