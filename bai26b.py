def sap_xep(so):
  chuoi_so = str(so)

  chuoi_sap_xep = ''.join(sorted(chuoi_so))

  ket_qua = int(chuoi_sap_xep)

  return ket_qua

so = int(input("Nhập số: "))

ket_qua = sap_xep(so)
print("Số sau khi sắp xếp:", ket_qua)