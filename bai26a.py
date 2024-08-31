a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a > b:
      a, b = b, a
if b > c:
      b, c = c, b
if a > b:
      a, b = b, a
print(a, b, c)