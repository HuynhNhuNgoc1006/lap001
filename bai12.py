def dinh_dang_ngay_thang_nam(ngay, thang, nam):
  

  dinh_dang = []
  dinh_dang.append(f"{ngay}/{thang}/{nam}")
  dinh_dang.append(f"{ngay}/{thang}/{str(nam)[2:]}")
  dinh_dang.append(f"{nam}/{thang}/{ngay}")
  return dinh_dang

# Nhập ngày, tháng, năm
ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))

# Định dạng và in kết quả
ket_qua = dinh_dang_ngay_thang_nam(ngay, thang, nam)
print("Các định dạng ngày tháng năm:")
for i, dinh_dang in enumerate(ket_qua, 1):
  print(f"{i}. {dinh_dang}")
  