def kiem_tra_gio_phut_giay(gio, phut, giay):
  
  if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    return True
  else:
    return False

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))

if kiem_tra_gio_phut_giay(gio, phut, giay):
  print("Giờ, phút, giây hợp lệ.")
else:
  print("Giờ, phút, giây không hợp lệ.")