num = int(input(">> 높이가 몇인 피라미드를 출력할까요? : "))
print(">> 높이가 {N}인 피라미드를 출력합니다.".format(N=num))
for j in range(1, num+1):
   x = int((2*(num-j))/2)
   print(" "*x,end="")
   print("*"*(2*j-1))
print(">> 매리 크리스마스;)")