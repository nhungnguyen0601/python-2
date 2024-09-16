# Dự án: Quản lý danh sách học sinh
# Yêu cầu: Viết chương trình cho phép người dùng thêm, xóa, và in danh sách học sinh bằng vòng lặp.
hocsinh =[]
while True:
    print("1. Them: \n2. Xoa: \n3. Hien thi ds: \n4. Thoat:")
    nhap = int(input ("Chon thao tac:"))
    if nhap ==1:
      name = input("Them hoc sinh:")
      hocsinh.append(name)
    elif nhap ==2:
        name = input("Xoa hoc sinh: ")
        if name not in hocsinh:
            print(f"{name} khong co trong danh sach hs")
        else:
            hocsinh.remove(name)
    elif nhap ==3:
        for hs in hocsinh:
            print(f"{hs}")
    elif nhap ==4:
        print("Thoat")
        break
    else:
        print("Error")

