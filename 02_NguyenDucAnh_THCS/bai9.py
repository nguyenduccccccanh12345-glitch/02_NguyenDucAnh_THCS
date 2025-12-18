n = int(input("Nhập kích thước ma trận vuông n: "))

a = []
i = 0
while i < n:
    hang = []
    j = 0
    while j < n:
        x = int(input("Nhập phần tử [" + str(i) + "][" + str(j) + "]: "))
        hang.append(x)
        j += 1
    a.append(hang)
    i += 1

tong = 0
i = 0
while i < n:
    j = 0
    while j < n:
        if i + j == n - 1:
            tong += a[i][j]
        j += 1
    i += 1

print("Tổng các phần tử trên đường chéo phụ là:", tong)