'''
선서 :  나는 양심에 따라 절대 부정행위를 하지 않겠습니다. 
부정행위 적발 시 모든 민사, 형사상의 법적책임을 지겠습니다. 
이름 최준수 (20230841), 2023년 12월 7일(목)
'''
import ISSN as isn
import pickle
D = False

class File_1:
    def __init__(self, file_name : str):
        """
        self.f_name : 파일 이름
        self.my_file : 파일을 open값
        """
        self.f_name = file_name
        print(self.f_name)
        self.my_file = open(self.f_name, 'r', encoding='euc-kr')

    def close_file(self):
        """
        사용자가 지정한 파일을 닫는다.
        """
        try :
            self.my_file.close()
        
        except Exception as e:
            print(">> 경고! close_file() : ", e)

    def read_file(self):
        """
        open file을 통해 저장된 my_file의 값을 line by line으로 받아온다.
        """
        print(">> "+str(self.f_name)+"에서 ISSN번호를 차례로 읽어옵니다.")
        self.text_list = []
        try:
            if D:
                print("\nr-1) read_file()")
            with open(self.f_name) as f:
                for each_line in f:
                    self.text_list.append(each_line)
            print(">> 화일에서 읽어온 내용 : ", self.text_list)
            for i in range(len(self.text_list)):
                self.text_list[i] = self.text_list[i].rstrip()
        except Exception as e:
            print("\n>> 경고! read_file() : ", e)

class MyFileException(Exception):
    """
    User-defined Exception handler를 이용해서 
    새 파일 my_new_notest.txt에 대하여 w mode으로 대응.
    """
    def __init__(self, msg):
        self.msg = msg
        if D:
            print("\nMyFileException : ",self.msg)
class makePickling:
    """
        pickling 관련 작업을 하는 클래스 입니다.
    """
    def __init__(self, my_dic):
        self.data = my_dic
    def pic(self):
        with open('certify_issn_number.pkl', 'wb') as f:
            print("\n>> Pickling을 시작합니다.")
            pickle.dump(self.data, f)
            print(">> Dump certify_issn_number.pkl 화일을 생성했습니다.")
    def loadpic(self):
        with open('certify_issn_number.pkl', 'rb') as f:
            print("\n>> Load : certify_issn_number.pkl 화일을 읽어옵니다.")
            my_list = pickle.load(f)
            print(">> Unpicked 결과입니다. : ", my_list)

class Main:
    def main(self):
        myFile = File_1("input_issn_list.txt")
        myFile.read_file()
        myIsn = isn.ISSN()
        count = 1
        dic_cert = {}
        print(">> ISSN code 검증을 시작합니다.")
        for i in myFile.text_list:
            print("\n>>",count,"번째 ISSN code : ", i)
            if myIsn.varifyISSN(i):
                    print(">> ISSN 코드 ",i,"은 (는) 검증되었습니다.")
                    dic_cert[i] = 'RIGHT'
            elif not myIsn.varifyISSN(i): #ISSN 코드가 아닌데 디짓코드가 달라서 그런건지, 아니면 잘못된 형식인지 모름
                if not myIsn.checkValue(): # 잘못된 형식임을 확인하는 코드 
                    myIsn.checkcheck() 
                else:
                    print(">> ISSN 코드 ",i,"은 (는) 검증되지 않았습니다.")
                    dic_cert[i] = 'WRONG' #딕셔너리를 생성해서 넣는다.
            count +=1
        print("\n>> 생성된 Dictionary입니다 : ", dic_cert)
        myPic = makePickling(dic_cert)
        myPic.pic()
        myPic.loadpic()
        
#main
myMain = Main()
myMain.main()


