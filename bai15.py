import math
a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
A1=((a+b)/(math.pow(a,1/3))+(math.pow(b,1/3)))-(math.pow(a*b,1/3))
A2=((math.pow(a,1/3))-(math.pow(b,1/3)))**2
Thuong=A1/A2
print("Kết quả là:",Thuong)