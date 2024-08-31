def doi_sang_giay(gio, phut, giay):
  

  tong_so_giay = gio * 3600 + phut * 60 + giay
  return tong_so_giay

gio_str = input("Nhập số giờ: ")
phut_str = input("Nhập số phút: ")
giay_str = input("Nhập số giây: ")

gio = int(gio_str.replace(str("h")," "))
phut = int(phut_str.replace(str("p")," "))
giay = int(giay_str.replace(str("s")," "))

tong_so_giay = doi_sang_giay(gio, phut, giay)

print(f"{gio_str} {phut_str} {giay_str} tương đương với {tong_so_giay} giây")