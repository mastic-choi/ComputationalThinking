error_Rate10 = ((2**10 - 10**3) / 10**3)*100
print(error_Rate10)
print("10bit로 표현하는 kilo와 실제 1,000과의 오차율은 %.1f%%입니다." %error_Rate10)
error_Rate20 = ((2**20 - 10**6) / 10**6)*100
print("20bit로 표현하는 mega와 실제 1,000,000과의 오차율은 %.4f%%입니다." %error_Rate20)
error_Rate30 = ((2**30 - 10**9) / 10**9)*100
print("30bit로 표현하는 giga와 실제 1,000,000,000과의 오차율은 %.7f%%입니다." %error_Rate30)