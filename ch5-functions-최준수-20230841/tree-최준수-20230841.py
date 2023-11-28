import turtle

s=turtle.Screen()
t=turtle.Turtle()
A = 30

def drawTree(t, lineLength):
    if lineLength>0:
        t.forward(lineLength)
        t.left(A)
        drawTree(t, lineLength - 10)

        t.right(A)
        t.right(A)
        drawTree(t, lineLength - 10)

        t.left(A)
        t.backward(lineLength)
def main():
    if __name__ == "__main__": #class variable가 main하고 같니?
        lineLength = 60
        t.left(90)
        drawTree(t, lineLength)

#main
main()