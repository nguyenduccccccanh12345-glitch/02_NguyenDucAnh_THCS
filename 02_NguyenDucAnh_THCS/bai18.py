n = int(input("Nhập số cặp key-value: "))

dic = {}

i = 0
while i < n:
    key = input("Nhập key: ")
    value = input("Nhập value: ")
    dic[key] = value
    i += 1

dao_nguoc = {}

for k in dic:
    v = dic[k]
    dao_nguoc[v] = k

print("Dictionary ban đầu:")
print(dic)

print("Dictionary sau khi đảo ngược:")
print(dao_nguoc)