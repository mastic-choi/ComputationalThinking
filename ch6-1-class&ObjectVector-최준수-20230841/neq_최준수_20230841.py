#D = False
D = True 

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __neq__(self, other): #not equal
        return self.x != other.x or self.y != other.y
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)    
    
class Main:
    def main(self):
        u = Vector2D(0,1)
        v = Vector2D(1,0)
        w = Vector2D(1,1)
        if D:
            print("1) print u = ", u)
            print("2) print v = ", v)
            print("3) print w = ", w)
        if D:
            print("7) Vector w와 Vector v가 같지 않다는 논리는 {}입니다.".format(u.__neq__(w)))
            print("5) Vector v와 Vector w의 합은 {}입니다.".format(v.__add__(w)))
            print("6) Vector w와 Vector u의 차는 {}입니다.".format(w.__sub__(u)))
            print("7) Vector w와 Vector v가 같다는 논리는 {}입니다.".format(w.__eq__(v)))

m = Main()
m.main()