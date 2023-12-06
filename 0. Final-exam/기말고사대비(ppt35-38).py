D = True
# D = False

import os.path

class File_1:
    def __init__(self, file_name : str):
        """
        self.f_name : 파일 이름
        self.my_file : 파일을 open값
        """
        if D: #echo check
            print("\ni-1) file_name : {}".format(file_name))
            print("i-2) Constructor에서 file을 r모드로 open")
        try:
            self.f_name = file_name
            self.my_file = open(self.f_name, 'r', encoding='utf-8')
        except:
            print("\n>> 경고!! 생성자 {}이 존재하지 않음!".format(file_name))

    def open_mode(self, mode : str):
        """
        텍스트 파일을 open한다. 단, 사용자가 입력한 mode가 따라 텍스트 open 모드를 변화해서 연다. mode는 str값이다.
        """
        try:
            if D:
                print("\no-1) open_mode() / file_name : {}, mode : {}".format(self.f_name, mode)) 
            if mode in ['r', 'a', 'w']:
                if D:
                    print("o-2) {}을 {} mode로 open".format(self.f_name, mode))
                self.my_file = open(self.f_name, mode, encoding='utf-8')
        except Exception as e:
            print(">> 경고! open_mode() : ", e)
    
    def close_file(self):
        """
        사용자가 지정한 파일을 닫는다.
        """
        try :
            if D:
                print("\nc-1) close_file()을 실행")
                print("c-2) {}을 close합니다.".format(self.my_file))
            self.my_file.close()
        
        except Exception as e:
            print(">> 경고! close_file() : ", e)

    def read_file(self):
        """
        open file을 통해 저장된 my_file의 값을 line by line으로 받아온다.
        """
        try:
            if D:
                print("\nr-1) read_file()")
            with open(self.f_name) as f:
                i = 1
                for each_line in f:
                    #each_line.rstrip() #각 줄에서 줄바꿈 문자를 제거
                    print(">> {}번 째 줄 내용 : {}".format(i, each_line))
                    i += 1
        except Exception as e:
            print("\n>> 경고! read_file() : ", e)

    def append(self):
        """
        새로운 값을 my_file에 추가한다.
        """
        try :
            if D:
                print("\na-1) append()")
                print("a-2) file name : {}".format(self.f_name))
            input_line = input("\n>> 추가하실 새로운 일정을 입력해 주세요 : ")
            input_line = "\n" + input_line
            self.open_mode('a')

            if D:
                print("\na-3) {}을 append 모드로 open".format(self.my_file))
            self.my_file.write(input_line)
            self.close_file()

        except Exception as e:
            print("\n>> 경고! append() : ", e)

    def write_file(self):
        """
        사용자의 my_file값을 local에 저장한다. 
        만약에 동일한 이름의 파일이 존재한다면 덮여쓰이지 않게 하기 위해 raise을 통해 오류를 발생시켜 usr에게 인지시킨다.
        """
        if D:
            print("\nw-1) write_file()")
            print("w-2) file name = {}".format(self.f_name))
        try :
            if os.path.isfile(self.f_name):
                if D:
                    print("w-3) User-defined Exception Handler 호출")
                raise MyFileException(">>> Warning) 동일한 이름의 파일이 이미 존재합니다.")
            else : #동일한 이름의 파일이 존재하지 않는다면~
                self.open_mode('w')
                self.write_contents()

        except MyFileException as e:
            if D:
                #print("w-4) e : ",e)
                pass
            answer = input("\n>>> 현존하는 파일을 새로운 내용으로 overwrite 하시겠습니까? Y or N : ")
            if answer in ['y', 'Y', "yes", "Yes", "YES"]:
                self.open_mode("w")
                self.write_contents()
            else :
                pass
    def write_contents(self):
        """
        write_file의 기능을 구현한다.
        """
        if D:
            print("\nwc-1) w 모드로 새로운 내용쓰기")
        self.my_file.write("새로운 파일이 생성되었습니다\n")
        self.my_file.write("모두 반갑습니다:)\n")
        self.my_file.write("열심히 공부합시다.:)\n")

        self.close_file()

    def __del__(self):
        """
        instantiation한 객체들의 소멸자.
        """
        try :
            if D:
                print("\nd-1) Destructor에서 {}을 close".format(self.my_file))
            self.my_file.close()
        except Exception as e:
            print("\n>> 경고! 소멸자에 오류가 있습니다. : ", e)

class MyFileException(Exception):
    """
    User-defined Exception handler를 이용해서 
    새 파일 my_new_notest.txt에 대하여 w mode으로 대응.
    """
    def __init__(self, msg):
        self.msg = msg
        if D:
            print("\nMyFileException : ",self.msg)

class Main():
    def main(self):
        #f_name = input("\n File명을 입력하세요 : ")
        f_name = "my_new_notes.txt"

        ex_file = File_1(f_name)
        ex_file.read_file()

        ex_file.append()
        ex_file.read_file()

        ex_file.write_file()
        ex_file.read_file()

#main

if __name__ == "__main__":
    if D:
        print("\n1) main")
    
    exe_main = Main()
    exe_main.main()

    if D:
        print("\n2) main End")