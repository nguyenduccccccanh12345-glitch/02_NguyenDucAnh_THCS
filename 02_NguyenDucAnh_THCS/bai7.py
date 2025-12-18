def tinh_tong_so_hoan_hao(a, b):
    tong = 0
    i = a

    while i <= b:
        tong_uoc = 0
        j = 1

        while j < i:
            if i % j == 0:
                tong_uoc += j
            j += 1

        if tong_uoc == i and i != 0:
            tong += i

        i += 1

    return tong

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

ket_qua = tinh_tong_so_hoan_hao(a, b)
print("Tổng các số hoàn hảo trong khoảng là:", ket_qua)