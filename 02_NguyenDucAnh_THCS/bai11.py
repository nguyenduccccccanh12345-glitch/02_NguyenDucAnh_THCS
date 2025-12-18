n = int(input("Nhập kích thước ma trận vuông n: "))

# Nhập ma trận
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

# Kiểm tra ma trận đối xứng
doi_xung = True
i = 0
while i < n:
    j = i + 1
    while j < n:
        if a[i][j] != a[j][i]:
            doi_xung = False
            break
        j += 1
    if not doi_xung:
        break
    i += 1

# In kết quả
if doi_xung:
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận không phải là ma trận đối xứng")