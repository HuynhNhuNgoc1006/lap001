import math

ban_kinh = float(input("Nhập bán kính hình tròn: "))
chu_vi = 2 * math.pi * ban_kinh

dien_tich = math.pi * ban_kinh**2

print("Chu vi hình tròn là:", chu_vi)
print("Diện tích hình tròn là:", dien_tich)