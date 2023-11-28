print(">> 삼각형의 세변의 값 a, b, c를 입력하세요")
print("     조건 : a <= b <= c")

a = float(input(">> a : "))
b = float(input("   b : "))
c = float(input("   c : "))

print("\n>> a = {}, b = {}, c = {}" .format(a, b, c))

if a <= b <= c:
    if a ** 2 + b**2 == c ** 2:
        print("\n>> 직각삼각형 입니다.")
    elif a ** 2 + b ** 2 > c ** 2 :
        print("\n>> 둔각삼각형 입니다.")
    else :
        print("\n>> 예각삼각형 입니다.")
else :
    print("\n$ a <= b <= c 의 조건을 만족해야 합니다.")