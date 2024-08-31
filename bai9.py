menu = {
    1: "Hủ tiếu",
    2: "Cháo lòng",
    3: "Bánh canh",
    4: "Bún riêu",
    5: "Phở bò"
}

while True:
    
    print("============ MENU =============")
    print("1. Hủ tiếu")
    print("2. Cháo lòng")
    print("3. Bánh canh")
    print("4. Bún riêu")
    print("5. Phở bò")
    print("==============================")
   

    lua_chon = input("Mời nhập lựa chọn: ")

    if lua_chon.isdigit():
        lua_chon = int(lua_chon)
        if 1 <= lua_chon <= len(menu):
            print(f"Bạn đã chọn: {menu[lua_chon]}")
            
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến", len(menu))
    else:
        print("Vui lòng nhập một số nguyên.")