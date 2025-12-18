s = input("Nhập chuỗi: ")

# Nhập n
n = int(input("Nhập n: "))

tu_hien_tai = ""
do_dai = 0

print("Các từ có độ dài lớn hơn", n, "là:")

for ch in s:
    if ch != ' ':
        tu_hien_tai += ch
        do_dai += 1
    else:
        
        if do_dai > n:
            print(tu_hien_tai)

        tu_hien_tai = ""
        do_dai = 0

if do_dai > n:
    print(tu_hien_tai)