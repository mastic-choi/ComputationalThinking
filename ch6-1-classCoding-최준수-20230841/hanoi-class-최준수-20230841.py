#D=False
D = True

class Hanoi:

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
    
class Main:
    def main(self, n):
        myHanoi = Hanoi()
        if D:
            print("\nA-1) Hanoi Class의 instantiation을 완료했습니다.")
        count_of_move = myHanoi.move(n)
        if D:
            print("A-2) 원반 개수가 {N}개 일 때, {C}번 원반을 옮겨야 합니다.\n".format(N=n, C = count_of_move))
        myHanoi.hanoi(n, "A", "B", "C")




n = int(input("1) 원반 개수가 몇인 하노이탑을 연산할까요? : "))
if D:
    print("2) 사용자가 입력하신 숫자는 {}입니다.".format(n))
main = Main()
if D:
    print("\n3) Main classs의 instantiation을 완료했습니다.")
main.main(n)