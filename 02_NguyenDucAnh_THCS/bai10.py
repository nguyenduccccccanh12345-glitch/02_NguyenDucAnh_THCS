m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

a = []
i = 0
while i < m:
    hang = []
    j = 0
    while j < n:
        x = int(input("Nhập phần tử [" + str(i) + "][" + str(j) + "]: "))
        hang.append(x)
        j += 1
    a.append(hang)
    i += 1

hang_max = 0
tong_max = None

i = 0
while i < m:
    tong = 0
    j = 0
    while j < n:
        tong += a[i][j]
        j += 1

    if tong_max is None or tong > tong_max:
        tong_max = tong
        hang_max = i

    i += 1

print("Hàng có tổng lớn nhất là hàng:", hang_max)
print("Tổng lớn nhất là:", tong_max)