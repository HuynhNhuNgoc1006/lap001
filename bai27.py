import math

def tinh_dien_tich_chu_vi(hinh):
 

  if hinh == 'v':
    # Hình vuông
    canh = float(input("Nhập độ dài cạnh: "))
    dien_tich = canh * canh
    chu_vi = 4 * canh
  elif hinh == 'n':
    # Hình chữ nhật
    chieu_dai = float(input("Nhập chiều dài: "))
    chieu_rong = float(input("Nhập chiều rộng: "))
    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)
  elif hinh == 't':
    # Hình tròn
    ban_kinh = float(input("Nhập bán kính: "))
    dien_tich = math.pi * ban_kinh * ban_kinh
    chu_vi = 2 * math.pi * ban_kinh
  else:
    print("Hình không hợp lệ!")
    return

  print("Diện tích:", dien_tich)
  print("Chu vi:", chu_vi)

# Nhập loại hình
hinh = input("Nhập hình (v: vuông, n: chữ nhật, t: tròn): ")

# Gọi hàm tính toán
tinh_dien_tich_chu_vi(hinh)