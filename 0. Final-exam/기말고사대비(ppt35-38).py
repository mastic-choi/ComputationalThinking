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
        """
        if D:
            print("\nw-1) write_file()")
            print("w-2) file name = {}".format(self.f_name))
        try :
            if os.path.isfile(self.f_name):
                if D:
                    print("w-3) User-defined Exception Handler 호출")
                raise MyFileExceoption(">>> Warning) 동일한 이름의 파일이 이미 존재합니다.")
            else :
                pass
        
        except MyFileExceoption as e:
            pass