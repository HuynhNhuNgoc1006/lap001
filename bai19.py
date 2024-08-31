a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
d = int(input("Nhập số thứ tư: "))

so_nho_nhat = a

if b < so_nho_nhat:
    so_nho_nhat = b
if c < so_nho_nhat:
    so_nho_nhat = c
if d < so_nho_nhat:
    so_nho_nhat = d

print("Số nhỏ nhất là:", so_nho_nhat)