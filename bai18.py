def cong_thoi_gian(gio1, phut1, giay1, gio2, phut2, giay2):
    

    tong_giay = gio1 * 3600 + phut1 * 60 + giay1 + gio2 * 3600 + phut2 * 60 + giay2

    gio = tong_giay // 3600
    phut = (tong_giay % 3600) // 60
    giay = tong_giay % 60

    return gio, phut, giay

def tru_thoi_gian(gio1, phut1, giay1, gio2, phut2, giay2):
    

    tong_giay1 = gio1 * 3600 + phut1 * 60 + giay1
    tong_giay2 = gio2 * 3600 + phut2 * 60 + giay2

    hieu_giay = tong_giay1 - tong_giay2

    gio = hieu_giay // 3600
    phut = (hieu_giay % 3600) // 60
    giay = hieu_giay % 60

    return gio, phut, giay


gio1 = int(input("Nhập giờ của thời gian 1: "))
phut1 = int(input("Nhập phút của thời gian 1: "))
giay1 = int(input("Nhập giây của thời gian 1: "))

gio2 = int(input("Nhập giờ của thời gian 2: "))
phut2 = int(input("Nhập phút của thời gian 2: "))
giay2 = int(input("Nhập giây của thời gian 2: "))


tong = cong_thoi_gian(gio1, phut1, giay1, gio2, phut2, giay2)
hieu = tru_thoi_gian(gio1, phut1, giay1, gio2, phut2, giay2)


print("Tổng hai khoảng thời gian là:", tong)
print("Hiệu hai khoảng thời gian là:", hieu)