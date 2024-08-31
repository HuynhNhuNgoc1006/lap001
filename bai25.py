chu_cai = input("Nhập một chữ cái: ")
print(chu_cai.upper() if chu_cai.islower() else chu_cai.lower() if chu_cai.isupper() else "Không phải chữ cái")