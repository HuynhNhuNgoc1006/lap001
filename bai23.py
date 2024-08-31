import math

def giai_phuong_trinh_bac_hai(a, b, c):
    
    if a == 0:
        print("Phương trình không phải là phương trình bậc hai.")
        return

    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1:.2f}, x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x:.2f}")
    else:
        print("Phương trình vô nghiệm")

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

giai_phuong_trinh_bac_hai(a, b, c)