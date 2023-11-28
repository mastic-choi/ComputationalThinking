#10진수 -> 2, 8, 16 진수 변수
x = 100000
print("%d is %s in binary " %(x, bin(x))) #100000 is 0b11000011010100000 in binary 
print("%d is %s in binary " %(x, oct(x))) #100000 is 0o303240 in binary 
print("%d is %s in binary " %(x, hex(x))) #100000 is 0x186a0 in binary 

#N진수 -> 10진수 변환 (2<=n and n<=32)
xb = "11000011010100000"
print("%s is %d in decimal " %(xb, int(xb, 2))) #11000011010100000 is 100000 in decimal 

xo = "303240"
print("%s is %d in deciaml " %(xo, int(xo, 8))) #303240 is 100000 in deciaml 

xh = "186a0"
print("%s is %d in decimal " %(xh, int(xh, 16))) #186a0 is 100000 in decimal 
