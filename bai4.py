import math
n=int(input("Nhập N="))
if 10<=n<=99:
 tong=n//10+n%10
 print(f"{n//10}+{n%10}={tong}")
else:
 print("Nhập số nguyên dương có 2 chữ số")