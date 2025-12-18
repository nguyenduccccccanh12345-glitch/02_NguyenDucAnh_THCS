n = int(input("Nhập số phần tử của list: "))

a = [12]
i = 0
while i < n:
    x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
    a.append(x)
    i += 1

k = int(input("Nhập k: "))

if n != 0:
    k = k % n

lan = 0
while lan < k:
    
    tam = a[n - 1]

    i = n - 1
    while i > 0:
        a[i] = a[i - 1]
        i -= 1

    a[0] = tam
    lan += 1

print("List sau khi dịch sang phải", k, "vị trí là:")
print(a)