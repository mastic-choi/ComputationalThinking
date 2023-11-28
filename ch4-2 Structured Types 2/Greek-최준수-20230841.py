#사용자에게 영문이름을 받기
usr_input = input("1) 한국어 표현을 알고싶은 로마자를 입력해주세요 : ")
print("2) 사용자가 입력하신 영문 로마자는 {ROME}입니다.".format(ROME = usr_input)) #echo checking

#사용자가 입력한 String을 toLower
engRome = usr_input.lower()

#로마자 dict 설정
rome = {'alpha': '알파', 'beta': '베타', 'gamma': '감마', 'delta': '델타', 'epsilon': '엡실론', 'zeta': '제타', 'eta': '에타', 'theta': '쎄타', 'iota': '요타', 'kappa': '카파', 'lambda': '람다', 'mu': '뮤', 'nu': '뉴', 'xi': '크싸이', 'omicron': '옴미크론', 'pi': '파이', 'rho': '로', 'sigma': '시그마', 'tau': '타우', 'upsilon': '입실론', 'phi': '파이', 'chi': '카이', 'psi': '프사이', 'omega': '오메가'}

#사용자가 입력한 값이 dic에 존재하는지 확인
D = True
while D:
    if engRome in rome.keys():
        D = False
        print("\n3) 사용자가 입력하신 {}은 dic에 존재합니다!".format(usr_input))
    else :
        print("\n3) 사용자가 입력하신 {}은 dic에 존재하지 않습니다... :(".format(usr_input))
        print("4) 프로그램을 종료합니다... :(")
        exit()

#해당하는 값 찾기
krRome = rome[engRome]
print("\n4) 사용자가 입력하신 로자마 {ENG}의 한국어 표현은 {KOR} 입니다.".format(ENG = usr_input, KOR = krRome))
print("\n5) 갑사합니다.")