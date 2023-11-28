x = 1024 # 0000 00100 0000 0000
print(">> 11th bit of",x, 1&(x>>10)) # 1
x = 4    # 0000 00000 0000 0100
print(">> 1st bit of",x, 1&(x>>0)) # 0
print(">> 2nd bit of",x, 1&(x>>1)) # 0
print(">> 3rd bit of",x, 1&(x>>2)) # 1