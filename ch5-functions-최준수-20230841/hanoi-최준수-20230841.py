def move(n): #원반의 개수가 n개 일 때, 몇 번 원반을 옮겨야 하는가 연산
    if n == 1:
        return 1
    else:
        return 1 + 2*move(n-1)

def hanoi(n, moveFrom, moveTemp, moveTo):
    if n == 1:
        print("{N}을 {F}에서 {T}으로 이동".format(N = n, F=moveFrom, T = moveTo))
        return 
    else :
        hanoi(n-1,moveFrom,moveTo,moveTemp)
        print("{N}을 {F}에서 {T}으로 이동".format(N = n, F = moveFrom, T = moveTo))
        hanoi(n-1,moveTemp,moveFrom,moveTo)
        print("{N}을 {T}에서 {F}으로 이동".format(N = n, T = moveTemp, F = moveFrom))

'''
하노이의 탑을 풀이하는 과정을 시각화
'''
tower = [[],[],[]] #빈 하노이의 탑을 생선한다.

def sortTower(): #하노이의 탑을 보기 좋게 정렬한다.
    tower[0].sort()
    tower[1].sort()
    tower[2].sort()

def movehanoi(x, moveFrom, moveTo): #하노이의 탑을 이동시키는 메서드를 시행하는 함수
    if x in tower[moveFrom]:
        tower[moveFrom].remove(x)
        tower[moveTo].append(x)
        sortTower()

def moveVisualization(n, moveFrom, moveTemp, moveTo): #하노이 탑에서 어떤 타워를 어디로 이동시킬지 연산하는 제귀 함수
    if n == 1:
        movehanoi(1, moveFrom, moveTo)
        print(tower)
        return
    else : 
        moveVisualization(n-1,moveFrom,moveTo,moveTemp)
        movehanoi(n, moveFrom, moveTo)
        print(tower)
        moveVisualization(n-1,moveTemp,moveFrom,moveTo)
        movehanoi(n, moveTemp, moveFrom)
        print(tower)

def visualization(n): #하노이의 탑을 생성하고 moveVisualization을 실행한다.
    tower[0] = list(range(1, n+1))
    print(tower)
    moveVisualization(n, 0, 1, 2)

def main():
    n = int(input("\n>> 원반 개수가 몇인 하노이탑을 연산할까요? : "))
    print(">> 사용자가 입력하신 숫자는 "+str(n)+"입니다.")
    count_of_move = move(n)
    hanoi(n, 'A', 'B', 'C')
    print(">> 원반 개수가 {N}일 때, {C}번 원반을 옮겨야 합니다.\n".format(N = n, C = count_of_move))
    print("\n>> 시각화를 시작합니다.")
    visualization(n)

#main
if __name__ == "__main__":
    main()