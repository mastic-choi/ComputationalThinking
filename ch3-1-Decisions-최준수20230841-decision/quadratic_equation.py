import math

print(">> 2차 방정식의 계수 A, B, C를 입력하세요.")
A = float(input("   A = "))
B = float(input("   B = "))
C = float(input("   C = "))

print("\n>> A = {}, B = {}, C = {}".format(A, B, C))

D = B * B - 4 * A * C
print(">> 판별식 D 값 = ", D)

if A == 0:
    print("\n>> x = ", -C/B)

if D == 0 :
    print("\n>> x = ", - B / (2.0 * A))

elif D > 0:
    print("\n>> x1 = ", (-B + math.sqrt(D)) / (2.0 * A))
    print(">>x2 = ", (-B - math.sqrt(D)) / (2.0 * A))

else : 
    print("\n 실근이 존재하지 않음")