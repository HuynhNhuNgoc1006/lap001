a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

so_lon_nhat = a

if b > so_lon_nhat:
    so_lon_nhat= b
if c > so_lon_nhat:
    so_lon_nhat = c

print("Số lớn nhất là:", so_lon_nhat)