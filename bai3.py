a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))


if b != 0:
 
  phan_nguyen = a // b
  phan_du = a % b
  print(f"Phần nguyên của {a} chia cho {b} là: {phan_nguyen}")
  print(f"Phần dư của {a} chia cho {b} là: {phan_du}")
else:
  print("Không thể chia cho 0")