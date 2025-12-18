n = int(input("Nhập số phần tử: "))

a = []
i = 0
while i < n:
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)
    i += 1

tong_chan = 0
tong_le = 0

i = 0
while i < n:
    if a[i] % 2 == 0:
        tong_chan += a[i]
    else:
        tong_le += a[i]
    i += 1

print("Tổng các số chẵn:", tong_chan)
print("Tổng các số lẻ:", tong_le)
