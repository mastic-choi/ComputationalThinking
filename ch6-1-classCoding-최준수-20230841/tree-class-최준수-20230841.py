D = True #Debug 기법
#D = False
import turtle
class Tree:
    
    def __init__(self):
        self.s = turtle.Screen()
        self.t = turtle.Turtle()
        self.angle = 30

    def drawTree(self, line_length):
        if line_length > 0:
            self.t.forward(line_length)
            self.t.left(self.angle)
            self.drawTree(line_length - 10)

            self.t.right(self.angle)
            self.t.right(self.angle)
            self.drawTree(line_length - 10)

            self.t.left(self.angle)
            self.t.backward(line_length)

class Main:
    def main(self):
        n = int(input(">> 나무의 초기 굵기를 몇으로 설정하시겠습니까? : "))
        if D:
            print("\n>> 입력하신 숫자는 {}입니다.".format(n))
        myTree = Tree()
        myTree.drawTree(n)
        input()

#main
m = Main()
m.main()