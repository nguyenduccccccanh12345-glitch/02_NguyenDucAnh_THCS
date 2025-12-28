import sys
import os

duong_dan = os.path.abspath("../thu_vien_chung")
sys.path.append(duong_dan)

from thu_vien_chung.xu_ly_so import kiem_tra_so_nguyen_to
so = int(input("Nhập một số:"))
if kiem_tra_so_nguyen_to(so):
    print(so,"là số nguyên tố")
else:
    print(so,"không phải là số nguyên tố")