n = int(input("Nhập số phần tử: "))

a = []
i = 0
while i < n:
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)
    i += 1

print("Danh sách sau khi loại bỏ phần tử trùng:")

i = 0
while i < n:
    x = a[i]

    trung = False
    j = 0
    while j < i:
        if a[j] == x:
            trung = True
            break
        j += 1

    if not trung:
        print(x, end=" ")
        i += 1