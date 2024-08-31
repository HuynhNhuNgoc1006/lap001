import math
gio,phut,giay=map(int,input("Nhập giờ, phút và giây:").split())
tong_giay=gio*3600+phut*60+giay
print(f"{tong_giay}giay")