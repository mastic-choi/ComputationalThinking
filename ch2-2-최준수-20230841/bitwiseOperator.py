print("23 & 5 : ", 23 & 5)
print("23 | 5 : ", 23 | 5)
print("23 ^ 5 : ", 23 ^ 5)
print("3 << 3 : ", 3 << 3)
print("32 >> 2 : ", 32 >> 2)



a = 16 + 4 + 2 + 1 #23
b = 4 + 1          #5
print("\n")
print(" a = ", bin(a)) #0b10111
print(" b = ", bin(b)) #0b101
print("\n")
print(" a & b = ", a & b, "Binary = ", bin(a&b)) #0b101
print(" a | b = ", a | b, "Binary = ", bin(a|b)) #0b10111
print(" a & b = ", a ^ b, "Binary = ", bin(a^b)) #0b10010