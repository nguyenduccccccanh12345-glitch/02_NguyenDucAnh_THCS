from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri

ds = [9,2,6,1,4,8]
danh_sach_td = sap_xep_tang_dan(ds)
print("Danh sách tăng dần là:",ds)

td = {"ten : Nguyễn Đức Anh"
      "tuoi : 18"
      "lop : DHKL19A2HN"}

gt = lay_gia_tri(td)

print("Gìa trị là :", td)