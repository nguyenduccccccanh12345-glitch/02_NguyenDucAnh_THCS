n = int(input("Nhập số phần tử: "))

a = []
i = 0
while i < n:
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)
    i += 1

max1 = a[0]
i = 1
while i < n:
    if a[i] > max1:
        max1 = a[i]
    i += 1

max2 = None
i = 0
while i < n:
    if a[i] < max1:
        if max2 is None or a[i] > max2:
            max2 = a[i]
    i += 1

if max2 is None:
    print("Không tồn tại giá trị lớn thứ hai")
else:
    print("Giá trị lớn thứ hai là:", max2)