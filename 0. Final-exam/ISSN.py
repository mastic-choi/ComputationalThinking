D = False
class ISSN:
    """
        ISSN의 검증에 관련된 전반적인 내용을 담고 있는 클래스 입니다.
    """
    def __init__(self, usr_input = '0027935K'):
        self.usr_input = usr_input
        if D:
            print("is-i-1) usr_ input : ", self.usr_input)
        self.input_list = list(self.usr_input)
        if D:
            print("is-i-2) 사용자가 입력한 self.usr_input을 리스트화: ", self.input_list)

    def checkValue(self): #디짓코드가 옳은 형식인지 파악해 TF를 리턴합니다.
        """
        사용자에게 입력받은 ISSN추정 코드의 마지막 digit코드가 옳은 것인지 인증한다.
        """
        if not self.input_list[-1] in ['0', 'X', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False
        else:
            return True
        
    def checkcheck(self): #형식을 파악하고 옳지 않은 형식이면 오류를 출력합니다.
        if not self.input_list[-1] in ['0', 'X', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if not self.input_list[0].isnumeric():
                myException("숫자나 X이외의 문자를 포함하고 있습니다.")
            else :
                myException("마지막 문자가 X가 아닙니다.")
        

    def calWeigth(self):
        weight = 0
        count = 0
        for i in self.input_list[:-1]: #인텍스로 for문을돌리고 인덱스로 호출로 값을 받는다.
            if i.isnumeric():
                num = int(i)
                weight = weight + num*(8-count)
            count+=1
        weight_remainder = weight%11
        if (11- weight_remainder) == 10:
            self.check_digit = 'X'
        elif (11 - weight_remainder) == 11:
            self.check_digit = '0'
        else :
            self.check_digit = str(11 - weight_remainder)
        return self.check_digit
    
    def varifyISSN(self, usr_input):
        self.__init__(usr_input)
        if self.checkValue():
            if  self.calWeigth() == self.input_list[-1]:
                return True
            else :
                return False
        else:
            return False
class myException(Exception):
    def __init__(self, msg):
        self.msg = msg
        print(">> Exception ) 잘못된 코드, ", msg)

if __name__ == "__main__":
    print("직접 실행했습니다.")
    myISSN = ISSN()
    if myISSN.varifyISSN('20493630'):
        print('검증됨')
    else:
        print('검증 안됨.')
        myISSN.checkcheck()
