import random

def sinh_so_ngau_nhien(a, b):
  """Sinh một số ngẫu nhiên trong khoảng từ a đến b (bao gồm cả a và b)

  Args:
    a: Giới hạn dưới
    b: Giới hạn trên

  Returns:
    Một số ngẫu nhiên trong khoảng đã cho
  """

  return random.randint(a, b)

# Nhập lựa chọn
lua_chon = input("Chọn khoang ban muon: \n "
                 "a. 0 đến 100\n"
                 "b. 50 đến 99\n"
                 "c. -39 đến 79\n"
                 "d. -79 đến -39\n"
                 "khoan ban muon chon la:")

# Sinh số ngẫu nhiên theo lựa chọn
if lua_chon == 'a':
  so_ngau_nhien = sinh_so_ngau_nhien(0, 100)
elif lua_chon == 'b':
  so_ngau_nhien = sinh_so_ngau_nhien(50, 99)
elif lua_chon == 'c':
  so_ngau_nhien = sinh_so_ngau_nhien(-39, 79)
elif lua_chon == 'd':
  so_ngau_nhien = sinh_so_ngau_nhien(-79, -39)
else:
  print("Lựa chọn không hợp lệ!")
  exit()
print("Số ngẫu nhiên:", so_ngau_nhien)

