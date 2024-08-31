a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a != 0:
    print(f"Phương trình có nghiệm duy nhất: x = {(-b/a):.2f}")
elif b != 0:
    print("Phương trình vô nghiệm")
else:
    print("Phương trình có vô số nghiệm")