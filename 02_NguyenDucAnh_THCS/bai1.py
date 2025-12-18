s = input("Nhập chuỗi: ")

# Khởi tạo biến đếm
so_chu_cai = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0

# Duyệt từng ký tự trong chuỗi
for ch in s:
    # Kiểm tra chữ cái (A-Z hoặc a-z)
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        so_chu_cai += 1

    # Kiểm tra chữ số (0-9)
    elif '0' <= ch <= '9':
        so_chu_so += 1

    # Các ký tự còn lại coi là ký tự đặc biệt
    else:
        so_ky_tu_dac_biet += 1

# In kết quả
print("Số ký tự chữ cái:", so_chu_cai)
print("Số ký tự chữ số:", so_chu_so)
print("Số ký tự đặc biệt:", so_ky_tu_dac_biet)
