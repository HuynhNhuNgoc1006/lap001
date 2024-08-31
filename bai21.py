so = int(input("Nhập một số: "))

so_chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

if 0 <= so <= 9:
    print(so_chu[so].title())
else:
    print("Không đọc được")