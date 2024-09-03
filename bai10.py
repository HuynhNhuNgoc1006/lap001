def tinh_so_nut(so_xe):
  
  tong_cac_chu_so = 0
  while so_xe > 0:
    chu_so = so_xe % 10
    tong_cac_chu_so += chu_so
    so_xe //= 10
  so_nut = tong_cac_chu_so % 10
  return so_nut


so_xe = int(input("Nhập số xe (4 chữ số): "))


so_nut = tinh_so_nut(so_xe)
print("Số nút của biển số xe là:", so_nut)
