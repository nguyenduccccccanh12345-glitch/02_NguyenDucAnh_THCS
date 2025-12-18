s = input("Nhập chuỗi: ")

ket_qua = ""
da_gap_khoang_trang = False

for ch in s:
    if ch != ' ':
        ket_qua += ch
        da_gap_khoang_trang = False
    else:

        if not da_gap_khoang_trang and ket_qua != "":
            ket_qua += ' '
            da_gap_khoang_trang = True

if ket_qua != "" and ket_qua[-1] == ' ':
    ket_qua = ket_qua[:-1]

print("Chuỗi sau khi xóa khoảng trắng thừa:")
print(ket_qua)