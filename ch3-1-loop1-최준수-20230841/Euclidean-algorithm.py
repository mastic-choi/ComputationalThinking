print(">> 두개의 수를 입력하시오. 큰 수를 먼저 입력하시요. 작은 수는 다음으로 입력하시오.")

large = int(input(">>> 큰 수 (large) : "))
small = int(input("    작은 수 (small) : "))

print("\n>> large = {L}, small ={S}".format(L=large, S=small))
print("\n>> {L}와 {S}의 최대공약수(GCD) : ".format(L=large, S=small), end = "")

while small != 0:
    x = large
    large = small
    small = x%large

print(large)