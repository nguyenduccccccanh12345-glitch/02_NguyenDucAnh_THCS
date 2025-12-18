n1 = int(input("Nhập số phần tử của dictionary 1: "))
dic1 = {}
i = 0
while i < n1:
    key = input("Nhập key: ")
    value = int(input("Nhập value: "))
    dic1[key] = value
    i += 1

n2 = int(input("Nhập số phần tử của dictionary 2: "))
dic2 = {}
i = 0
while i < n2:
    key = input("Nhập key: ")
    value = int(input("Nhập value: "))
    dic2[key] = value
    i += 1

ket_qua = {}

for k in dic1:
    ket_qua[k] = dic1[k]

for k in dic2:
    if k in ket_qua:
        ket_qua[k] = ket_qua[k] + dic2[k]
    else:
        ket_qua[k] = dic2[k]

print("Dictionary sau khi gộp:")
print(ket_qua)
