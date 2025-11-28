a=[]
# 50 thg dau la vdv
# 10 thg sau la hlv
# 10 thg sau la nhan vien dieu hanh dởm
# 10 thg sau la chu tich
# for _ in range(100):
#     a.append(input())
import random
# print(a)
# stt=0
# tenhopdong=["Hợp đồng thi đấu","Hợp đồng huấn luyện","Hợp đồng lao động","Hợp đồng quản lý"]
# print("INSERT INTO HopDong (MaHopDong, TenHopDong, MoTa, ThoiHan)")
# for i in range(70,80):
#     stt=i+1
#     mahopdong=f"'HD{stt:03d}'"
#     ran=random.randint(36,72)
#     while(ran%6!=0):
#         ran=random.randint(6,110)
#     print("("+mahopdong,f"'{tenhopdong[2]}'",f"'{tenhopdong[2]+" theo tháng"}'",\
#                     str(ran)+"),",sep=", ")

address=['Phường Cầu Kho, Quận 1, TP. Hồ Chí Minh', 'Xã Minh Quang, Huyện Ba Vì, Hà Nội', 'Phường Bình Trị Đông, Quận Bình Tân, TP. Hồ Chí Minh', 'Xã Tân Thành, Huyện Yên Thành, Tỉnh Nghệ An', 'Phường Thanh Xuân Trung, Quận Thanh Xuân, Hà Nội', 'Phường Hạ Đình, Quận Thanh Xuân, Hà Nội', 'Xã Đại Đồng, Huyện Thạch Thất, Hà Nội', 'Phường Linh Đông, Quận Thủ Đức, TP. Hồ Chí Minh', 'Xã Lương Sơn, Huyện Ninh Sơn, Tỉnh Ninh Thuận', 'Phường Tân An, Quận Ninh Kiều, TP. Cần Thơ', 'Phường Hải Châu 1, Quận Hải Châu, TP. Đà Nẵng', 'Xã Phú Túc, Huyện Châu Thành, Tỉnh Bến Tre', 'Phường Thọ Quang, Quận Sơn Trà, TP. Đà Nẵng', 'Xã Tam Hiệp, Huyện Châu Thành, Tỉnh Tiền Giang', 'Phường Hòa Khánh Nam, Quận Liên Chiểu, TP. Đà Nẵng', 'Phường Thạnh Mỹ Lợi, Quận 2, TP. Hồ Chí Minh', 'Xã Bạch Đằng, Huyện Tiên Lãng, TP. Hải Phòng', 'Phường Hưng Lợi, Quận Ninh Kiều, TP. Cần Thơ', 'Phường Dĩ An, Thành phố Dĩ An, Tỉnh Bình Dương', 'Xã Tân Tiến, Huyện Chương Mỹ, Hà Nội', 'Phường Nguyễn Du, Quận Hai Bà Trưng, Hà Nội', 'Xã Vạn Ninh, Huyện Quảng Ninh, Tỉnh Quảng Bình', 'Phường Trường Thọ, Quận Thủ Đức, TP. Hồ Chí Minh', 'Xã Lâm Sơn, Huyện Ninh Sơn, Tỉnh Ninh Thuận', 'Phường Bình Hưng Hòa A, Quận Bình Tân, TP. Hồ Chí Minh', 'Xã Cẩm Lĩnh, Huyện Ba Vì, Hà Nội', 'Phường Phước Long A, Quận 9, TP. Hồ Chí Minh', 'Xã Kim Chung, Huyện Đông Anh, Hà Nội', 'Phường Thảo Điền, Quận 2, TP. Hồ Chí Minh', 'Phường Tam Phước, Thành phố Biên Hòa, Tỉnh Đồng Nai']
a=['Nguyễn Văn An', 'Trần Thị Bích Ngọc', 'Lê Minh Quân', 'Phạm Thị Hương', 'Đỗ Ngọc Trâm', 'Bùi Văn Long', 'Hoàng Thị Mai Anh', 'Vũ Quang Hải', 'Nguyễn Thị Thu Hằng', 'Trần Mạnh Dũng', 'Lê Thị Thanh Thảo', 'Phạm Quốc Tuấn', 'Đặng Thị Kim Chi', 'Ngô Xuân Phúc', 'Dương Thị Nhung', 'Nguyễn Hữu Phước', 'Trịnh Thị Lan', 'Lý Hải Nam', 'Võ Thị Tuyết', 'Phan Minh Hoàng', 'Tạ Thị Thu Trang', 'Đỗ Văn Bình', 'Bùi Thị Thuý', 'Hoàng Văn Tiến', 'Vũ Thị Phương', 'Nguyễn Minh Khang', 'Trần Thị Minh Thu', 'Lê Công Hậu', 'Phạm Ngọc Bảo', 'Đặng Văn Đức', 'Ngô Thanh Huyền', 'Dương Văn Quang', 'Nguyễn Hải Yến', 'Trịnh Văn An', 'Lý Quang Dũng', 'Võ Minh Anh', 'Phan Thị Hạnh', 'Tạ Văn Long', 'Đỗ Thị Thùy Linh', 'Bùi Quốc Đạt', 'Hoàng Thị Thu Hương', 'Vũ Hồng Sơn', 'Nguyễn Thị Hoa', 'Trần Văn Minh', 'Lê Phương Thảo', 'Phạm Thế Anh', 'Đặng Thị Hải', 'Ngô Đức Vinh', 'Dương Thị Lan Anh', 'Nguyễn Mạnh Cường', 'Trịnh Thị Ngọc', 'Lý Văn Hưng', 'Võ Hoàng Lan', 'Phan Quỳnh Mai', 'Tạ Đình Tú', 'Đỗ Thị Hằng Nga', 'Bùi Thanh Tùng', 'Hoàng Ngọc Hà', 'Vũ Văn Lợi', 'Nguyễn Văn Kiên', 'Trần Thị Bảo Ngọc', 'Lê Hữu Tuấn', 'Phạm Văn Bảo', 'Đặng Quốc Bảo', 'Ngô Thị Thúy', 'Dương Minh Hà', 'Nguyễn Thị Mỹ Duyên', 'Trịnh Đức Minh', 'Lý Khánh Linh', 'Võ Văn Hoài', 'Phan Hữu Thắng', 'Tạ Thị Lan', 'Đỗ Minh Khánh', 'Bùi Thị Mai', 'Hoàng Hải Đăng', 'Vũ Thị Loan', 'Nguyễn Văn Thắng', 'Trần Thị Hồng', 'Lê Anh Khoa', 'Phạm Thị Nhung', 'Đặng Huy Hoàng', 'Ngô Minh Tuấn', 'Dương Thị Phương', 'Nguyễn Minh Hương', 'Trịnh Văn Thái', 'Lý Thị Mai', 'Võ Đức Huy', 'Phan Ngọc Ánh', 'Tạ Thị Thu', 'Đỗ Đình Phúc', 'Bùi Thanh Hằng', 'Hoàng Văn Thanh', 'Vũ Thị Tuyết', 'Nguyễn Thị Hương', 'Trần Hữu Phước', 'Lê Quỳnh Chi', 'Phạm Văn Lộc', 'Đặng Minh Anh', 'Ngô Thị Hoa', 'Dương Văn Sơn']




def randombirthdate():
    from datetime import datetime, timedelta

    # Giới hạn ngày bắt đầu và kết thúc
    start_date = datetime(1989, 1, 1)
    end_date = datetime(2005, 12, 31)

    # Tạo số ngẫu nhiên để tính toán ngày
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)

    # Tính toán ngày ngẫu nhiên
    random_date = start_date + timedelta(days=random_days)

    # In ra ngày ngẫu nhiên
    return random_date.strftime('%Y-%m-%d')


def randombirthdatequanly():
    from datetime import datetime, timedelta

    # Giới hạn ngày bắt đầu và kết thúc
    start_date = datetime(1980, 1, 1)
    end_date = datetime(1990, 12, 31)

    # Tạo số ngẫu nhiên để tính toán ngày
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)

    # Tính toán ngày ngẫu nhiên
    random_date = start_date + timedelta(days=random_days)

    # In ra ngày ngẫu nhiên
    return random_date.strftime('%Y-%m-%d')




import random
stt=0


def nhansu_quanly():
    print("INSERT INTO NhanSu (MaNhanSu, HoVaTen, NgaySinh, DiaChi, Luong, CCCD, MaHopDong, MaQuanLy) VALUES")
    for i in range(70,80):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        hovaten=a[i]
        ngaysinh=randombirthdatequanly()
        diachi=address[random.randint(0,len(address)-1)]
        luong=(random.randint(30000000,50000000)//100000)*100000
        cccd=random.randint(100000000000,999999999999)
        mahopdong=f"'HD{stt:03d}'"
        maquanly="NULL"

        print("("+manhansu,f"'{hovaten}'",f"'{ngaysinh}'",f"'{diachi}'",luong,\
            f"'{cccd}'",f"{mahopdong}", f"{maquanly}),",sep=", ")


def nhansu_vandongvien():
    print("INSERT INTO NhanSu (MaNhanSu, HoVaTen, NgaySinh, DiaChi, Luong, CCCD, MaHopDong, MaQuanLy) VALUES")
    for i in range(50):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        hovaten=a[i]
        ngaysinh=randombirthdate()
        diachi=address[random.randint(0,len(address)-1)]
        luong=(random.randint(1000000,30000000)//100000)*100000
        limit=random.randint(1,10)
        if limit<8:
            luong=(random.randint(5000000,12000000)//100000)*100000
        cccd=random.randint(100000000000,999999999999)
        mahopdong=f"'HD{stt:03d}'"
        maquanly=f"'NS071'"

        print("("+manhansu,f"'{hovaten}'",f"'{ngaysinh}'",f"'{diachi}'",luong,\
            f"'{cccd}'",f"{mahopdong}", f"{maquanly}),",sep=", ")

def nhansu_hlv():
    print("INSERT INTO NhanSu (MaNhanSu, HoVaTen, NgaySinh, DiaChi, Luong, CCCD, MaHopDong, MaQuanLy) VALUES")
    for i in range(50,60):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        hovaten=a[i]
        ngaysinh=randombirthdatequanly()
        diachi=address[random.randint(0,len(address)-1)]
        luong=(random.randint(20000000,30000000)//100000)*100000
        cccd=random.randint(100000000000,999999999999)
        mahopdong=f"'HD{stt:03d}'"
        ran=random.randint(1,3)
        maquanly=f"'NS072'"
        if ran==2: maquanly=f"'NS073'"
        if ran==3: maquanly=f"'NS074'"

        print("("+manhansu,f"'{hovaten}'",f"'{ngaysinh}'",f"'{diachi}'",luong,\
            f"'{cccd}'",f"{mahopdong}", f"{maquanly}),",sep=", ")

def nhansu_nhansuquen():
    print("INSERT INTO NhanSu (MaNhanSu, HoVaTen, NgaySinh, DiaChi, Luong, CCCD, MaHopDong, MaQuanLy) VALUES")
    for i in range(60,70):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        hovaten=a[i]
        ngaysinh=randombirthdate()
        diachi=address[random.randint(0,len(address)-1)]
        luong=(random.randint(5000000,9000000)//100000)*100000
        cccd=random.randint(100000000000,999999999999)
        mahopdong=f"'HD{stt:03d}'"
        ran=random.randint(5,10)
        maquanly=f"'NS080'"
        if ran!=10: maquanly=f"'NS0{70+ran}'"

        print("("+manhansu,f"'{hovaten}'",f"'{ngaysinh}'",f"'{diachi}'",luong,\
            f"'{cccd}'",f"{mahopdong}", f"{maquanly}),",sep=", ")

def Vandongvien():
    thanhtichlist=["Vô địch Đông Nam á 2019","Á Quân Thế giới 2020","Huy chương đồng Châu Á 2023","Huy chương Bạc thế vận hội Quốc gia 2017",\
                "Huy chương vàng thế giới 2015","Á Quân Đông Nam Á 2016","Vô địch Châu Á 2022","Huy chương đồng Thể thao quốc tế 2024",\
                    "Vô địch Đông Nam á 2020","Á Quân Thế giới 2021","Vô địch Châu Á 2024","Huy chương Bạc thế vận hội Quốc gia 2019"]
    montt=['Bóng đá','Bóng chuyền','Bóng rổ','Điền kinh','Cầu lông','Bơi lội','Bóng bàn','Võ thuật','Cử tạ','Đua xe đạp']
    ttsk=["Rất tốt","Tốt","Khá","Chấn thương"]
    print("INSERT INTO NhanSu (MaNhanSu, HoVaTen, NgaySinh, DiaChi, Luong, CCCD, MaHopDong, MaQuanLy) VALUES")
    for i in range(0,11):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[0]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS051'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ") 
    for i in range(11,22):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[1]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS052'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ")

    j=2
    for i in range(22,31):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[j]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS05{j+1}'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ")
    j+=1
    for i in range(31,34):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[j]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS05{j+1}'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ")
    j+=1
    for i in range(34,37):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[j]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS05{j+1}'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ")
    j+=1
    for i in range(37,39):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[j]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS05{j+1}'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ")
    j+=1
    for i in range(39,42):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[j]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS05{j+1}'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ")
    j+=1
    for i in range(42,45):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[j]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS05{j+1}'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ")
    j+=1
    for i in range(45,47):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[j]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS05{j+1}'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ")
    j+=1
    for i in range(47,50):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        monthethao=montt[j]
        thongtinsuckhoe=ttsk[random.randint(0,2)]
        ran=random.randint(1,10)
        if ran>8: thongtinsuckhoe=ttsk[3]
        thanhtich=thanhtichlist[random.randint(0,len(thanhtichlist)-1)]
        mahlv=f"'NS05{j+1}'"
        print("("+manhansu,f"'{monthethao}'",f"'{thongtinsuckhoe}'",f"'{thanhtich}'",\
           f"{mahlv}),",sep=", ")
    j+=1
    
def NhanvienDieuhanh():
    vitrilist=['Trợ lý','Chuyên viên','Nhân viên']
    phongbanlist=['Kế hoạch','Dịch vụ','Hành chính','Vận hành','Môi trường','Quản lý VDV','Quản lý HLV','Quản lý nhân sự','Kinh doanh','Đào tạo']
    for i in range(60,70):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        vt=vitrilist[random.randint(0,2)]
        phongban="Vận hành"
        print("("+manhansu,f"'{vt}'", f"'{phongban}'),",sep=", ")
    for i in range(70,80):
        stt=i+1
        manhansu=f"'NS{stt:03d}'"
        vt="Quản lý"
        phongban="Vận hành"
        if stt==71: phongban="Quản lý VDV"
        if stt==72 or stt==73 or stt==74: phongban="Quản lý HLV"
        

        print("("+manhansu,f"'{vt}'", f"'{phongban}'),",sep=", ")

    
def Khangia():
    tinhtanh=['An Giang', 'Bà Rịa – Vũng Tàu', 'Bắc Giang', 'Bắc Kạn', 'Bến Tre', 'Bình Dương', 'Bình Định', 'Bình Phước', 'Bình Thuận', 'Cà Mau', 'Cao Bằng', 'Cần Thơ', 'Đà Nẵng', 'Đắk Lắk', 'Đắk Nông', 'Điện Biên', 'Đồng Nai', 'Đồng Tháp', 'Gia Lai', 'Hà Giang', 'Hà Nam', 'Hà Nội', 'Hải Dương', 'Hải Phòng', 'Hòa Bình', 'Hậu Giang', 'Hồ Chí Minh', 'Hưng Yên', 'Khánh Hòa', 'Kiên Giang', 'Kon Tum', 'Lai Châu', 'Lâm Đồng', 'Lạng Sơn', 'Lào Cai', 'Long An', 'Nam Định', 'Nghệ An', 'Ninh Bình', 'Ninh Thuận', 'Phú Thọ', 'Phú Yên', 'Quảng Bình', 'Quảng Nam', 'Quảng Ngãi', 'Quảng Ninh', 'Quảng Trị', 'Sóc Trăng', 'Sơn La', 'Tây Ninh', 'Thái Bình', 'Thái Nguyên', 'Thanh Hóa', 'Thừa Thiên Huế', 'Tiền Giang', 'TP Hồ Chí Minh', 'Trà Vinh', 'Tuyên Quang', 'Vĩnh Long', 'Vĩnh Phúc', 'Yên Bái', 'Phú Quý', 'Bắc Ninh']
    ten=['Nguyễn Anh Tuấn', 'Trần Minh Tuấn', 'Phạm Thu Hà', 'Lê Minh Tâm', 'Vũ Hoàng Nam', 'Đỗ Thị Thanh', 'Hồ Ngọc Sơn', 'Nguyễn Thị Lan', 'Lê Đức Hải', 'Trần Thị Thu Hương', 'Phan Quang Huy', 'Võ Thị Mỹ Duyên', 'Nguyễn Thị Lý', 'Đặng Minh Tâm', 'Lê Quang Hieu', 'Trần Anh Duy', 'Phạm Thị Mai', 'Vũ Minh Thành', 'Nguyễn Thị Kim Chi', 'Bùi Văn Tân', 'Đoàn Thị Mai', 'Lê Hải Anh', 'Trần Thị Lan Anh', 'Hoàng Minh Cường', 'Phan Quân Tùng', 'Đỗ Minh Quân', 'Lê Thị Kim Ngân', 'Nguyễn Hải Nam', 'Trương Thanh Vân', 'Hoàng Thị Mai', 'Nguyễn Thị Thanh Tú', 'Trần Thị Minh Tuyết', 'Đặng Minh Đức', 'Nguyễn Thị Bích Ngọc', 'Phạm Hoàng Anh', 'Hồ Nguyễn Khánh Huy', 'Trương Lý Ngọc Anh', 'Bùi Thị Bích Thuận', 'Lê Quang Trí', 'Nguyễn Minh Tuấn', 'Hoàng Văn Tùng', 'Đỗ Minh Trí', 'Phạm Thanh Sơn', 'Vũ Bích Ngọc', 'Nguyễn Kim Dung', 'Trần Quốc Việt', 'Lê Hoàng Linh', 'Phan Minh Nhật', 'Đoàn Thị Lan', 'Hoàng Thanh Sơn', 'Lê Đức Hoàng', 'Trần Thị Thanh Trúc', 'Nguyễn Thị Phương Thảo', 'Bùi Minh Ngọc', 'Đỗ Thiên Thanh', 'Lê Tấn Tài', 'Nguyễn Thị Tuyết Mai', 'Phạm Thanh Hương', 'Hồ Minh Tuấn', 'Trương Thị Thanh Vân', 'Phan Thanh Hòa', 'Lê Thanh Tâm', 'Nguyễn Anh Huy', 'Trần Ngọc Diễm', 'Phan Minh Thịnh', 'Bùi Thị Thanh Tuyền', 'Nguyễn Thị Hoài Thu', 'Đỗ Minh Cường', 'Lê Thiên Hoàng', 'Trương Thị Lan Anh', 'Vũ Anh Hào', 'Đặng Thị Kim Oanh', 'Trần Minh Tuấn', 'Hoàng Quang Hưng', 'Nguyễn Thị Mai Hương', 'Phan Ngọc Thiên', 'Lê Quang Duy', 'Trần Thị Minh Chi', 'Vũ Thanh Vân', 'Phạm Minh Tâm', 'Nguyễn Thị Lan Anh', 'Đoàn Thanh Tùng', 'Lê Thanh Long', 'Trần Quang Tùng', 'Hoàng Thuận Vũ', 'Phan Văn Trường', 'Hồ Bích Thuận', 'Nguyễn Minh Long', 'Lê Thị Thanh Trúc', 'Đoàn Thanh Ngọc', 'Trương Tường Vi', 'Phạm Thiên Kim', 'Nguyễn Tiến Dũng', 'Bùi Minh Hieu', 'Trần Thị Cẩm Vân', 'Lê Duy Anh', 'Nguyễn Bảo Minh', 'Phan Thị Thanh Hương', 'Hồ Thị Thanh Hằng', 'Trần Minh Thiện']
    ten2=['Trần Đăng Khoa', 'Phạm Bảo Châu', 'Nguyễn Quốc Thịnh', 'Đặng Thị Hoài Thương', 'Lê Thanh Bình', 'Vũ Thị Thu Trang', 'Nguyễn Văn Khánh', 'Trần Ngọc Huyền', 'Phạm Văn Hậu', 'Nguyễn Thị Khánh Ly', 'Hoàng Quốc Bảo', 'Đỗ Ngọc Minh', 'Lê Quang Hà', 'Phan Thị Cẩm Tú', 'Trần Đình Nam', 'Nguyễn Thị Tâm', 'Phạm Tuấn Kiệt', 'Lê Thị Mỹ Linh', 'Hồ Ngọc Quỳnh', 'Nguyễn Thị Thu Phương', 'Trần Thanh Hương', 'Đặng Văn Quý', 'Lê Hữu Thắng', 'Bùi Thị Minh', 'Hoàng Thị Phương Lan', 'Nguyễn Phúc Hưng', 'Trần Bảo Ngọc', 'Phạm Thị Thu Thủy', 'Đỗ Văn Trung', 'Nguyễn Hoàng Dương', 'Lê Văn Tiến', 'Trần Ngọc Tài', 'Hoàng Thị Bích Ngọc', 'Nguyễn Trọng Khôi', 'Vũ Văn Hoàng', 'Đỗ Thị Thu', 'Lê Bích Thủy', 'Phạm Đình Long', 'Trần Thị Thanh Bình', 'Nguyễn Hải Đăng', 'Bùi Đình Quân', 'Lê Thanh Hải', 'Phan Thị Như Quỳnh', 'Nguyễn Thị Hồng', 'Trần Đức Kiên', 'Nguyễn Văn Phong', 'Đặng Thị Bích Ngân', 'Lê Thị Lan Anh', 'Hoàng Minh Đức', 'Phạm Minh Khoa', 'Nguyễn Thành Nam', 'Trần Văn Phúc', 'Nguyễn Văn Tài', 'Phạm Ngọc Anh', 'Lê Quốc Tuấn', 'Nguyễn Phương Linh', 'Hồ Ngọc Lan', 'Vũ Thị Phương', 'Phan Văn Hà', 'Lê Hồng Sơn', 'Trần Văn Dũng', 'Nguyễn Thị Hoa', 'Đỗ Thanh Tâm', 'Lê Văn Hưng', 'Phạm Đức Tài', 'Nguyễn Hữu Nghĩa', 'Trần Ngọc Khoa', 'Phan Nhật Minh', 'Lê Hoài An', 'Bùi Quốc Khánh', 'Nguyễn Ngọc Minh', 'Lê Anh Thư', 'Đặng Hữu Nam', 'Nguyễn Thị Quỳnh Anh', 'Hoàng Ngọc Anh', 'Lê Thị Thảo', 'Trần Quốc Hoàn', 'Phạm Văn Long', 'Nguyễn Ngọc Diệp', 'Bùi Thị Ngọc Hà', 'Trần Phúc Thịnh', 'Lê Tuấn Minh', 'Phan Thị Lan', 'Vũ Thị Hòa', 'Nguyễn Thị Mai Linh', 'Trần Thị Thúy', 'Đỗ Phương Nam', 'Phạm Thị Dung', 'Lê Đức Duy', 'Nguyễn Hải Phong', 'Hồ Văn Sơn', 'Phan Ngọc Ánh', 'Trần Quang Linh', 'Nguyễn Đình Tùng', 'Lê Anh Đức', 'Bùi Minh Đạt', 'Phạm Thanh Tùng', 'Nguyễn Đức Hòa', 'Trần Thị Kim Chi', 'Nguyễn Thị Thu Hà']
    ten3=['Nguyễn Trọng Hiếu', 'Lê Ngọc Ánh', 'Trần Văn Đạt', 'Phạm Thị Kim Hằng', 'Vũ Quang Minh', 'Đặng Ngọc Sơn', 'Nguyễn Minh Phương', 'Hoàng Văn Hải', 'Lê Thị Hồng Nhung', 'Nguyễn Văn Bảo', 'Phạm Thanh Hải', 'Trần Thị Thu Hà', 'Bùi Đình Hoàn', 'Nguyễn Thị Vân Anh', 'Lê Trung Kiên', 'Phạm Văn Khôi', 'Hoàng Anh Dũng', 'Nguyễn Quang Hưng', 'Trần Bảo Linh', 'Phan Đăng Khoa', 'Lê Thị Ánh Tuyết', 'Đỗ Văn Hoàng', 'Nguyễn Khánh Toàn', 'Trần Văn Cường', 'Lê Văn Quân', 'Phạm Minh Hòa', 'Nguyễn Thị Lệ Quyên', 'Trần Thị Thanh Mai', 'Hoàng Tùng Dương', 'Phan Thị Thu', 'Nguyễn Ngọc Trâm', 'Trần Thanh Phong', 'Lê Khánh Linh', 'Vũ Văn Bách', 'Nguyễn Ngọc Hùng', 'Đỗ Quỳnh Như', 'Lê Thị Hoa', 'Nguyễn Mạnh Cường', 'Trần Ngọc Hà', 'Hoàng Thị Thanh Thúy', 'Phạm Thị Kim Oanh', 'Nguyễn Văn Hiền', 'Lê Tấn Phúc', 'Trần Hải Đăng', 'Phan Văn Đại', 'Vũ Đức Mạnh', 'Đặng Thị Ngọc Lan', 'Nguyễn Hoàng Phúc', 'Lê Văn Đạt', 'Trần Thị Cẩm Nhung', 'Nguyễn Thị Thanh', 'Phạm Văn Khánh', 'Hoàng Quốc Thịnh', 'Trần Ngọc Thạch', 'Lê Thị Minh Phượng', 'Nguyễn Văn Khôi', 'Đỗ Thị Lan Anh', 'Nguyễn Trọng Nghĩa', 'Phan Đình Vũ', 'Lê Văn Đức', 'Trần Thị Thu Thảo', 'Nguyễn Hoàng An', 'Lê Thị Ngọc Mai', 'Vũ Minh Ngọc', 'Nguyễn Văn Thắng', 'Phạm Văn Đông', 'Nguyễn Thị Hoàng Oanh', 'Hoàng Đình Tuấn', 'Lê Quốc Dũng', 'Trần Thị Mai Anh', 'Phạm Minh Hải', 'Nguyễn Thị Cúc', 'Trần Khắc Tâm', 'Lê Bảo Trâm', 'Phan Thị Bảo', 'Nguyễn Minh Huy', 'Hoàng Văn Khoa', 'Đỗ Thị Yến', 'Trần Phương Anh', 'Lê Minh Tuấn', 'Nguyễn Tùng Lâm', 'Phạm Quang Vinh', 'Lê Văn Dương', 'Nguyễn Ngọc Quân', 'Trần Thị Thanh Dung', 'Nguyễn Hữu Bình', 'Phạm Hồng Quang', 'Lê Văn Nam', 'Nguyễn Thị Hạnh', 'Trần Ngọc Tâm', 'Phạm Văn Hùng', 'Nguyễn Thị Thanh Hằng', 'Lê Thị Tố Uyên', 'Đỗ Quang Anh', 'Trần Đức Trung', 'Nguyễn Văn Luân', 'Hoàng Văn Lợi', 'Phạm Hữu Tài', 'Lê Minh Sơn', 'Nguyễn Khánh Hòa']
    ten4=['Nguyễn Anh Khoa', 'Lê Thị Thu Hương', 'Trần Thị Quỳnh', 'Phạm Ngọc Thảo', 'Bùi Anh Tuấn', 'Hồ Thị Hương', 'Lê Thanh Phương', 'Nguyễn Hoàng Duy', 'Trần Tiến Đạt', 'Vũ Hương Lan', 'Nguyễn Bảo Trung', 'Lê Minh Hiền', 'Đỗ Bích Ngọc', 'Trần Quốc Toàn', 'Phan Quang Trung', 'Hoàng Thị Lan', 'Nguyễn Đức Sơn', 'Bùi Minh Tuấn', 'Trần Quang Minh', 'Lê Thị Thu Trang', 'Nguyễn Thị Hồng Nhung', 'Vũ Hoàng Quân', 'Đỗ Thị Tường Vi', 'Trần Đình Huy', 'Lê Huyền Trang', 'Phan Minh Thiện', 'Nguyễn Hoàng Dũng', 'Trần Thị Lan Anh', 'Lê Minh Khang', 'Đỗ Quang Hậu', 'Vũ Thanh Sơn', 'Nguyễn Minh Nhật', 'Lê Tự Trung', 'Trần Ngọc Hằng', 'Phan Tài Lộc', 'Nguyễn Thiện Nhân', 'Lê Thị Thắm', 'Hoàng Tăng Cường', 'Đặng Thị Mỹ Linh', 'Trần Duy Phát', 'Lê Thanh Trúc', 'Phan Huyền Trang', 'Vũ Trọng An', 'Nguyễn Thiết Hoàng', 'Đỗ Thị Hoài Anh', 'Lê Đức Duy', 'Trần Thu Hằng', 'Phạm Bích Thảo', 'Nguyễn Hoàng Việt', 'Bùi Văn Thịnh', 'Lê Minh Hùng', 'Trần Hữu Đức', 'Nguyễn Bảo Khoa', 'Hoàng Thị Tâm', 'Phan Thị Thu Hằng', 'Trần Tiến Tuấn', 'Đặng Minh Phúc', 'Lê Văn Kiên', 'Nguyễn Tấn Đức', 'Trần Thị Thanh Bình', 'Lê Thị Bích Lan', 'Nguyễn Thị Tố Lan', 'Phạm Tuấn Khoa', 'Trần Kim Hoàng', 'Bùi Đức Minh', 'Nguyễn Thị Thanh Tú', 'Lê Bích Thảo', 'Hoàng Anh Khoa', 'Phan Trọng Hưng', 'Đỗ Thị Quý', 'Trần Quốc Minh', 'Nguyễn Thanh Thiện', 'Lê Quang Hiếu', 'Vũ Thị Thùy Linh', 'Đoàn Thiên Bình', 'Lê Thanh Sơn', 'Trần Quang Đức', 'Phan Trần Khải', 'Nguyễn Thái Hưng', 'Lê Thị Diễm Quỳnh', 'Trần Hữu Duy', 'Nguyễn Thị Duyên', 'Phạm Duy Anh', 'Lê Tất Thái', 'Hoàng Bích Thảo', 'Nguyễn Minh Vương', 'Trần Thị Kim Lan', 'Bùi Quang Tùng', 'Đỗ Ngọc Hào', 'Lê Đức Sơn', 'Trần Tiến Dũng', 'Nguyễn Tiến Minh', 'Lê Văn Hảo', 'Vũ Đình Toàn', 'Đặng Đức Tài', 'Nguyễn Minh Phúc', 'Trần Hữu Khang', 'Phan Ngọc Hoàng', 'Lê Văn Khánh', 'Hoàng Bảo Anh']
    for i in range(400,1400):
        makg=f"'KG{i+1:03d}'"
        tenkg=ten4[random.randint(0,99)]
        dc=tinhtanh[random.randint(0,62)]
        sdt="09"+str(random.randint(10000000,99999999))
        print("("+makg,f"'{tenkg}'",f"'{dc}'", f"'{sdt}'),",sep=", ")


def randombirthdatebtgannhat():
    from datetime import datetime, timedelta

    # Giới hạn ngày bắt đầu và kết thúc
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    # Tạo số ngẫu nhiên để tính toán ngày
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)

    # Tính toán ngày ngẫu nhiên
    random_date = start_date + timedelta(days=random_days)

    # In ra ngày ngẫu nhiên
    return random_date.strftime('%Y-%m-%d')

def randombirthdatebttieptheo():
    from datetime import datetime, timedelta

    # Giới hạn ngày bắt đầu và kết thúc
    start_date = datetime(2024, 12, 10)
    end_date = datetime(2025, 6, 30)

    # Tạo số ngẫu nhiên để tính toán ngày
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)

    # Tính toán ngày ngẫu nhiên
    random_date = start_date + timedelta(days=random_days)

    # In ra ngày ngẫu nhiên
    return random_date.strftime('%Y-%m-%d')


def Santhidau():
    sanlist=['Sân bóng đá', 'Sân bóng rổ', 'Sân tennis', 
    'Hồ bơi Olympic', 'Sân cầu lông Nhà thi đấu', 'Sân chạy điền kinh', 
    'Khu tập thể hình', 'Sân bóng chuyền', 'Khu tập bắn', 'Khu luyện tập phía Đông', 'Nhà thi đấu trung tâm', 
    'Sân đa năng']
    sanlist2 = [
    6000,  # Sân bóng đá
    500,       # Sân bóng rổ
    400,       # Sân tennis
    1250,           # Hồ bơi Olympic
    81,              # Sân cầu lông Nhà thi đấu
    7000,  # Sân chạy điền kinh
    400,     # Khu tập thể hình
    162,             # Sân bóng chuyền
    2500,    # Khu tập bắn
    1000,     # Khu luyện tập phía Đông
    8000,  # Nhà thi đấu trung tâm
    1500    # Sân đa năng
    
]
    for i in range(12):
        masan=f"'S{i+1:03d}'"
        tensan=sanlist[i]


        nbtgannha=randombirthdatebtgannhat()
        nbttiep=randombirthdatebttieptheo()
        ttvl=sanlist2[i]
        print("("+masan,f"'{tensan}'",ttvl,f"'{nbtgannha}'", f"'{nbttiep}'),",sep=", ")


def Trandau():
    sandaulist=[]
    timelist=[90,60,48,10,30,30,30,30,30,180]
    montt=['Bóng đá','Bóng chuyền','Bóng rổ','Điền kinh','Cầu lông','Bơi lội','Bóng bàn','Võ thuật','Cử tạ','Đua xe đạp']
    tentranlist=["Chung kết","Bán kết","Tứ kết","Vòng loại"]
    
    for j in range (10):
        stt=1
        for k in range(10):
            ck=1
            bk=2
            tk=4
            vl=random.randint(1,3)
            for i in range(tk+bk+vl+ck):
                matran=f"'TD{stt:03d}'"
                stt+=1
                magiaidau=f"'GD{j+1:03d}'"
                sttmonthi=k
                monthidau=montt[sttmonthi]
                timethidau=timelist[sttmonthi]
                if ck>0:
                    ck-=1
                    tentran=tentranlist[0]+" "+monthidau
                elif bk>0:
                    bk-=1
                    tentran=tentranlist[1]+" "+monthidau
                elif tk>0:
                    tk-=1
                    tentran=tentranlist[2]+" "+monthidau
                elif vl>0:
                    vl-=1
                    tentran=tentranlist[3]+" "+monthidau
            
                ketqua="Hoàn thành xuất sắc"

                print("("+matran,f"{magiaidau}",f"'{tentran}'",f"'{monthidau}'",timethidau,
                    f"'{ketqua}'),",sep=", ")

def ve():
    stt=1
    loaivelist=["Vip","Thường","Sinh viên","Gia đình"]
    vitri=['Hàng dưới','Hàng giữa','Hàng trên']
    for i in range(800,1800):
        mave=f"'VE{i+1:03d}'"
        ran=random.randint(1,10)
        if ran<=2: 
            loaive=loaivelist[0]
        elif ran<=7:loaive=loaivelist[1]
        elif ran<=9:loaive=loaivelist[2]
        else: loaive=loaivelist[3]
        vt=vitri[random.randint(0,len(vitri)-1)]
        makg=f"'KG{random.randint(1,400):03d}'"
        maquy=f"'QT{random.randint(1,20):03d}'"
        matran=f"'TD{random.randint(1,72):03d}'"
        magiai=f"'GD{random.randint(1,10):03d}'"
        print("("+mave,f"'{loaive}'",f"'{vt}'",makg,maquy,matran,
                    f"{magiai}),",sep=", ")

def giave():
    stt=1
    loaivelist=["Vip","Gia đình","Thường","Sinh viên"]
    vitri=['Hàng dưới','Hàng giữa','Hàng trên']

    cost=[200,170,150,140,120,100,90,80,70,60,50,40]
    stt=0
    for i in loaivelist:
        for j in vitri:
            lv=i
            vt=j
            price=cost[stt]*1000
            stt+=1
            print("("+f"'{lv}'",f"'{vt}'",
                    f"{price}),",sep=", ")


def sdtnhansu():
    for i in range(230):
        manhansu=f"'NS{random.randint(1,80):03d}'"
        sdt="09"+str(random.randint(10000000,99999999))
        print("("+manhansu,
                f"'{sdt}'),",sep=", ")

def thietbidonvi():
    tb=["Dụng cụ thể thao đa dụng","Trang thiết bị vệ sinh và bảo trì","Hệ thống quản lý và thiết bị điện tử","Trang thiết bị an toàn và hỗ trợ","Trang thiết bị cho sân ngoài trời","Trang thiết bị phòng tập gym và thể hình","Hệ thống chiếu sáng và âm thanh","Hệ thống sân tập và thi đấu đa năng"]

    for i in range(10):
        madv=f"'DVC{i+1:03d}'"
        print("("+madv,
                f"'{tb[0]}'),",sep=", ")
    for i in range(10):
        sotb=random.randint(1,3)
        se=set()
        while len(se)<sotb:
            se.add(random.randint(1,len(tb)-1))
        for j in se:
            madv=f"'DVC{i+1:03d}'"
            print("("+madv,
                    f"'{tb[j]}'),",sep=", ")

def randombirthdatensx():


    from datetime import datetime, timedelta

    # Giới hạn ngày bắt đầu và kết thúc
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 6, 30)

    # Tạo số ngẫu nhiên để tính toán ngày
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)

    # Tính toán ngày ngẫu nhiên
    random_date = start_date + timedelta(days=random_days)

    # In ra ngày ngẫu nhiên
    return random_date.strftime('%Y-%m-%d')

def randombirthdatehsd():
    from datetime import datetime, timedelta

    # Giới hạn ngày bắt đầu và kết thúc
    start_date = datetime(2024, 12, 1)
    end_date = datetime(2025, 12, 31)

    # Tạo số ngẫu nhiên để tính toán ngày
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)

    # Tính toán ngày ngẫu nhiên
    random_date = start_date + timedelta(days=random_days)

    # In ra ngày ngẫu nhiên
    return random_date.strftime('%Y-%m-%d')


def trangtbcsvc():
    stt=1
    tenThietbilist=[# Trang thiết bị cho môn bóng đá
    "Cầu môn và lưới",
    "Quả bóng đá đạt chuẩn",
    "Đồng phục thi đấu và tập luyện",
    "Giày bóng đá và các thiết bị bảo vệ như bọc ống đồng",

    # Trang thiết bị cho môn bóng rổ
    "Rổ bóng rổ và trụ bóng rổ có thể điều chỉnh độ cao",
    "Bóng rổ đạt chuẩn",
    "Đồng phục thi đấu",
    "Tấm chắn sân và lưới bóng rổ",

    #tennis
    "Lưới tennis",
    "Cột lưới tennis",
    "Bảng điểm sân tennis",
    "Bàn ghế cho trọng tài",

    # Trang thiết bị cho môn bơi lội
    "Phao bơi và dụng cụ hỗ trợ tập luyện",
    "Đồng hồ bấm giờ điện tử",
    "Hệ thống lọc nước và thiết bị làm sạch hồ bơi",
    "Bục nhảy và cầu nhảy",


    # Trang thiết bị cho môn cầu lông
    "Lưới cầu lông và cột lưới",
    "Vợt cầu lông và cầu lông (shuttlecock)",
    "Giày cầu lông chuyên dụng",
    "Thảm sân cầu lông",


    # Trang thiết bị cho môn điền kinh
    "Rào chắn chạy vượt rào",
    "Bục xuất phát",
    "Dụng cụ đẩy tạ, ném lao, và ném đĩa",
    "Thảm nhảy cao và nhảy xa",

    # Trang thiết bị cho môn thể hình và gym
    "Máy chạy bộ, máy đạp xe, máy tập đa năng",
    "Tạ tay, tạ đòn, và thanh tạ",
    "Ghế tập bụng, ghế tập tạ",
    "Các máy tập cơ như máy kéo lưng, máy đẩy ngực, và máy kéo cáp"

    # Trang thiết bị cho môn thể dục dụng cụ
    ]

    tblist2=[ # Trang thiết bị cho môn bóng chuyền
    "Lưới bóng chuyền",
    "Bóng chuyền",
    "Giày và đồng phục chuyên dụng",
    "Cột lưới có thể điều chỉnh",

    # Trang thiết bị cho môn bắn cung và bắn súng
    "Cung tên và bia bắn",
    "Súng hơi, bia bắn điện tử (cho môn bắn súng)",
    "Trang phục và phụ kiện bảo hộ",
    "Dụng cụ hỗ trợ ngắm"]

    tblist3=[
     # Nha thi dau trung tam
    "Camera giám sát an ninh",
    "Hệ thống báo cháy và báo động",
    "Cửa kiểm soát an ninh",
    "Đèn pha LED công suất lớn cho sân bãi ngoài trời",
    "Đèn chiếu sáng trong nhà",
    "Hệ thống điều hòa không khí",
    "Hệ thống quạt thông gió",

    #San da nang
    "Loa phát thanh ngoài trời và trong nhà",
    "Microphone và hệ thống âm thanh",
    "Ghế dài cho huấn luyện viên và vận động viên",
    "Xà đơn, xà kép",
    "Thảm tập thể dục",
    "Các thiết bị như cầu thăng bằng, nhảy sào, và vòng treo",
    
    #khu luyen tap phia dong
    "Máy chạy bộ",
    "Máy đạp xe",
    "Tạ tay, tạ đòn",
    "Máy tập cơ ngực, cơ lưng, cơ chân",
    "Dụng cụ tập đa năng",
    ]


    stt=0
    for i in range(7):
        for j in range(4):
            stt+=1
            mathietbi=f"'TB{stt:03d}'"
            tenThietbi=tenThietbilist[stt-1]
            thongsokithuat="NULL"
            soluong=random.randint(5,10)
            nsx=randombirthdatensx()
            hsd=randombirthdatehsd()
            madvi=f"'DVC{random.randint(1,10):03d}'"

            print("("+mathietbi,f"'{tenThietbi}'",thongsokithuat,
                    soluong,f"'{nsx}'",f"'{hsd}'",
                        f"{madvi}),",sep=", ")
    cnt=1
    for i in range(2):
        for j in range(4):
            stt+=1
            mathietbi=f"'TB{stt:03d}'"
            tenThietbi=tblist2[cnt-1]
            cnt+=1
            thongsokithuat="NULL"
            soluong=random.randint(5,10)
            nsx=randombirthdatensx()
            hsd=randombirthdatehsd()
            madvi=f"'DVC{random.randint(1,10):03d}'"

            print("("+mathietbi,f"'{tenThietbi}'",thongsokithuat,
                    soluong,f"'{nsx}'",f"'{hsd}'",
                        f"{madvi}),",sep=", ")
    cnt=1
    for i in range(3):
        a=[7,6,5]
        for j in range(a[i]):
            stt+=1
            mathietbi=f"'TB{stt:03d}'"
            tenThietbi=tblist3[cnt-1]
            cnt+=1
            thongsokithuat="NULL"
            soluong=random.randint(5,10)
            nsx=randombirthdatensx()
            hsd=randombirthdatehsd()
            madvi=f"'DVC{random.randint(1,10):03d}'"

            print("("+mathietbi,f"'{tenThietbi}'",thongsokithuat,
                    soluong,f"'{nsx}'",f"'{hsd}'",
                        f"{madvi}),",sep=", ")
    
def matbvamasan():
    stt=1
    tenThietbilist=[# Trang thiết bị cho môn bóng đá
    "Cầu môn và lưới",
    "Quả bóng đá đạt chuẩn",
    "Đồng phục thi đấu và tập luyện",
    "Giày bóng đá và các thiết bị bảo vệ như bọc ống đồng",

    # Trang thiết bị cho môn bóng rổ
    "Rổ bóng rổ và trụ bóng rổ có thể điều chỉnh độ cao",
    "Bóng rổ đạt chuẩn",
    "Đồng phục thi đấu",
    "Tấm chắn sân và lưới bóng rổ",

    #tennis
    "Lưới tennis",
    "Cột lưới tennis",
    "Bảng điểm sân tennis",
    "Bàn ghế cho trọng tài",

    # Trang thiết bị cho môn bơi lội
    "Phao bơi và dụng cụ hỗ trợ tập luyện",
    "Đồng hồ bấm giờ điện tử",
    "Hệ thống lọc nước và thiết bị làm sạch hồ bơi",
    "Bục nhảy và cầu nhảy",


    # Trang thiết bị cho môn cầu lông
    "Lưới cầu lông và cột lưới",
    "Vợt cầu lông và cầu lông (shuttlecock)",
    "Giày cầu lông chuyên dụng",
    "Thảm sân cầu lông",


    # Trang thiết bị cho môn điền kinh
    "Rào chắn chạy vượt rào",
    "Bục xuất phát",
    "Dụng cụ đẩy tạ, ném lao, và ném đĩa",
    "Thảm nhảy cao và nhảy xa",

    # Trang thiết bị cho môn thể hình và gym
    "Máy chạy bộ, máy đạp xe, máy tập đa năng",
    "Tạ tay, tạ đòn, và thanh tạ",
    "Ghế tập bụng, ghế tập tạ",
    "Các máy tập cơ như máy kéo lưng, máy đẩy ngực, và máy kéo cáp"

    # Trang thiết bị cho môn thể dục dụng cụ
    ]

    tblist2=[ # Trang thiết bị cho môn bóng chuyền
    "Lưới bóng chuyền",
    "Bóng chuyền",
    "Giày và đồng phục chuyên dụng",
    "Cột lưới có thể điều chỉnh",

    # Trang thiết bị cho môn bắn cung và bắn súng
    "Cung tên và bia bắn",
    "Súng hơi, bia bắn điện tử (cho môn bắn súng)",
    "Trang phục và phụ kiện bảo hộ",
    "Dụng cụ hỗ trợ ngắm"]

    tblist3=[
     # Nha thi dau trung tam
    "Camera giám sát an ninh",
    "Hệ thống báo cháy và báo động",
    "Cửa kiểm soát an ninh",
    "Đèn pha LED công suất lớn cho sân bãi ngoài trời",
    "Đèn chiếu sáng trong nhà",
    "Hệ thống điều hòa không khí",
    "Hệ thống quạt thông gió",

    #San da nang
    "Loa phát thanh ngoài trời và trong nhà",
    "Microphone và hệ thống âm thanh",
    "Ghế dài cho huấn luyện viên và vận động viên",
    "Xà đơn, xà kép",
    "Thảm tập thể dục",
    "Các thiết bị như cầu thăng bằng, nhảy sào, và vòng treo",
    
    #khu luyen tap phia dong
    "Máy chạy bộ",
    "Máy đạp xe",
    "Tạ tay, tạ đòn",
    "Máy tập cơ ngực, cơ lưng, cơ chân",
    "Dụng cụ tập đa năng",
    ]


    stt=0
    for i in range(7):
        for j in range(4):
            stt+=1
            mathietbi=f"'TB{stt:03d}'"
            masan=f"'S{i+1:03d}'"

            print("("+mathietbi,
                        f"{masan}),",sep=", ")
    cnt=1
    for i in range(2):
        for j in range(4):
            stt+=1
            mathietbi=f"'TB{stt:03d}'"
            masan=f"'S{i+8:03d}'"

            print("("+mathietbi,
                        f"{masan}),",sep=", ")
    cnt=1
    for i in range(3):
        a=[7,6,5]
        for j in range(a[i]):
            stt+=1
            mathietbi=f"'TB{stt:03d}'"
            masan=f"'S{i+10:03d}'"

            print("("+mathietbi,
                        f"{masan}),",sep=", ")
    

def hopdongchitra():
    tenhopdong=["Hợp đồng cung cấp và lắp đặt hệ thống",
    "Hợp đồng mua sắm trang bị thể thao",
    "Hợp đồng lắp đặt hệ thống ghế ngồi khán đài sân vận động",
    "Hợp đồng thỏa thuận cung cấp thiết bị và bảo trì định kỳ khu liên hợp",
    "Hợp đồng cung cấp dụng cụ thi đấu",
    "Hợp đồng cam kết dịch vụ hậu mãi cho thiết bị thể thao",
    "Hợp đồng thỏa thuận nguyên tắc cung cấp dụng cụ thi đấu thể thao"]
    for i in range(80,120):
        stt=i+1
        mahopdong=f"'HD{stt:03d}'"
        ran=random.randint(1,5)
        hd=random.randint(0,len(tenhopdong)-1)
        print("("+mahopdong,f"'Hợp đồng hợp tác'",f"'{tenhopdong[hd]+" theo năm"}'",\
                        str(ran)+"),",sep=", ")

def chitietchitra():
    hinhthuc=["Tiền mặt trực tiếp","Thanh toán quốc tế","Chuyển khoản ngân hàng"]
    mang=[1,2,7,8,9,10,11,12,13,14,15,17,18,20]
    for i in range(40):
        mahopdong=f"'HD{random.randint(81,120):03d}'"
        maquy=f"'QT{mang[random.randint(0,len(mang)-1)]:03d}'"
        madv=f"'DVC{random.randint(1,10):03d}'"
        htct=f"'{hinhthuc[random.randint(0,2)]}'"
        print("("+mahopdong,maquy,madv,\
                        htct+"),",sep=", ")
        
def chitietdieuhanh():
    tasks = [
    "Lên kế hoạch và tổ chức (xác định thời gian, địa điểm, lịch trình chi tiết; lập kế hoạch quản lý rủi ro)",
    "Quản lý nhân sự (phân công và giám sát nhân viên, tình nguyện viên, trọng tài)",
    "Điều phối và giám sát trận đấu (theo dõi lịch trình, xử lý sự cố, đảm bảo tuân thủ quy định)",
    "Tổ chức cơ sở vật chất và trang thiết bị (kiểm tra, bảo dưỡng trước khi giải đấu diễn ra)",
    "Quản lý tài chính (theo dõi chi phí, lập ngân sách, quản lý nguồn lực tài chính)",
    "Đăng ký và quản lý đội thi đấu (xác minh thông tin, đảm bảo tuân thủ quy định)",
    "Quản lý thông tin và truyền thông (phối hợp quảng bá, cập nhật kết quả trên phương tiện truyền thông)",
    "Hỗ trợ khán giả và an ninh (đảm bảo an ninh, hỗ trợ y tế, sắp xếp khán đài)",
    "Giám sát và xử lý khiếu nại (tiếp nhận và giải quyết khiếu nại, đảm bảo công bằng)",
    "Đánh giá và rút kinh nghiệm (thu thập phản hồi, lập báo cáo tổng kết)"
    ]
    staff_tasks = [
    "Hỗ trợ công tác chuẩn bị sân bãi và thiết bị thi đấu",
    "Hỗ trợ ghi nhận kết quả và báo cáo điểm số",
    "Hướng dẫn và hỗ trợ người tham gia giải đấu",
    "Thực hiện nhiệm vụ lễ tân, đón tiếp khách mời và khán giả",
    "Đảm bảo an ninh tại khu vực thi đấu",
    "Hỗ trợ công tác hậu cần như cung cấp nước uống, thực phẩm, và vật tư y tế",
    "Dọn dẹp và giữ vệ sinh khu vực thi đấu và khán đài",
    "Kiểm tra và bảo trì thiết bị trước và sau trận đấu",
    "Hỗ trợ đội ngũ trọng tài và ban tổ chức trong quá trình diễn ra giải đấu",
    "Thực hiện các nhiệm vụ phát sinh theo yêu cầu của ban tổ chức"
    ]


    for i in range(70):
        magiai=f"'GD{random.randint(1,10):03d}'"
        mns=random.randint(61,80)
        manhansu=f"'NS{mns:03d}'"
        if mns<81:
            task=staff_tasks[random.randint(0,len(staff_tasks)-1)]
        else:
            task=tasks[random.randint(0,len(tasks)-1)]
        print("("+magiai,manhansu,
                        f"'{task}'"+"),",sep=", ")
        


def chitietthamgiathidau():
    for i in range(200):
        mavdv=f"'NS{random.randint(1,50):03d}'"
        msk=f"'SK{random.randint(1,15):03d}'"
        quyhotro=[3,4,6,13,16,18,19,20]
        mquy=f"'QT{quyhotro[random.randint(0,len(quyhotro)-1)]:03d}'"
        tien=random.randint(18000000,40000000)//100000 * 100000
        print("("+mavdv,msk,mquy,
                        f"{tien}"+"),",sep=", ")
        

def chitiettrandau():
    tenThietbilist=[# Trang thiết bị cho môn bóng đá
    "Cầu môn và lưới",
    "Quả bóng đá đạt chuẩn",
    "Đồng phục thi đấu và tập luyện",
    "Giày bóng đá và các thiết bị bảo vệ như bọc ống đồng",

    # Trang thiết bị cho môn bóng rổ
    "Rổ bóng rổ và trụ bóng rổ có thể điều chỉnh độ cao",
    "Bóng rổ đạt chuẩn",
    "Đồng phục thi đấu",
    "Tấm chắn sân và lưới bóng rổ",

    #tennis
    "Lưới tennis",
    "Cột lưới tennis",
    "Bảng điểm sân tennis",
    "Bàn ghế cho trọng tài",

    # Trang thiết bị cho môn bơi lội
    "Phao bơi và dụng cụ hỗ trợ tập luyện",
    "Đồng hồ bấm giờ điện tử",
    "Hệ thống lọc nước và thiết bị làm sạch hồ bơi",
    "Bục nhảy và cầu nhảy",


    # Trang thiết bị cho môn cầu lông
    "Lưới cầu lông và cột lưới",
    "Vợt cầu lông và cầu lông (shuttlecock)",
    "Giày cầu lông chuyên dụng",
    "Thảm sân cầu lông",


    # Trang thiết bị cho môn điền kinh
    "Rào chắn chạy vượt rào",
    "Bục xuất phát",
    "Dụng cụ đẩy tạ, ném lao, và ném đĩa",
    "Thảm nhảy cao và nhảy xa",

    # Trang thiết bị cho môn thể hình và gym
    "Máy chạy bộ, máy đạp xe, máy tập đa năng",
    "Tạ tay, tạ đòn, và thanh tạ",
    "Ghế tập bụng, ghế tập tạ",
    "Các máy tập cơ như máy kéo lưng, máy đẩy ngực, và máy kéo cáp",

     # Trang thiết bị cho môn bóng chuyền
    "Lưới bóng chuyền",
    "Bóng chuyền",
    "Giày và đồng phục chuyên dụng",
    "Cột lưới có thể điều chỉnh",

    # Trang thiết bị cho môn bắn cung và bắn súng
    "Cung tên và bia bắn",
    "Súng hơi, bia bắn điện tử (cho môn bắn súng)",
    "Trang phục và phụ kiện bảo hộ",
    "Dụng cụ hỗ trợ ngắm"

    # Trang thiết bị cho môn thể dục dụng cụ
    ]



    tblist3=[
     # Nha thi dau trung tam
    "Camera giám sát an ninh",
    "Hệ thống báo cháy và báo động",
    "Cửa kiểm soát an ninh",
    "Đèn pha LED công suất lớn cho sân bãi ngoài trời",
    "Đèn chiếu sáng trong nhà",
    "Hệ thống điều hòa không khí",
    "Hệ thống quạt thông gió",

    #San da nang
    "Loa phát thanh ngoài trời và trong nhà",
    "Microphone và hệ thống âm thanh",
    "Ghế dài cho huấn luyện viên và vận động viên",
    "Xà đơn, xà kép",
    "Thảm tập thể dục",
    "Các thiết bị như cầu thăng bằng, nhảy sào, và vòng treo",
    
    #khu luyen tap phia dong
    "Máy chạy bộ",
    "Máy đạp xe",
    "Tạ tay, tạ đòn",
    "Máy tập cơ ngực, cơ lưng, cơ chân",
    "Dụng cụ tập đa năng",
    ]
    sandaulist=[]
    timelist=[90,60,48,10,30,30,30,30,30,180]
    montt=['Bóng đá','Bóng rổ',"Tennis",'Bơi lội','Cầu lông','Điền kinh',
    'Cử tạ','Bóng chuyền','Bắn súng']
    tentranlist=["Chung kết","Bán kết","Tứ kết","Vòng loại"]

    thelethidau=["Thi đấu đến hết giờ, tính tỉ số",
    "Đấu 5 set, đội nào thắng 3 set trước thì chiến thắng",
    "Thi đấu đến hết giờ, tính tỉ số",
    "Vận động viên về đích sớm nhất vô địch",
    "Đấu 3 set, đội nào thắng 2 set trước thì chiến thắng",
    "Tính vận động viên về đích sớm nhất",
    "Vận động viên có thành tích cử giật và cử đẩy tốt nhất chiến thắng",
    "Đấu 5 set, đội nào thắng 3 set trước thì chiến thắng",
    "Vận động viên có điểm cao nhất trong 3 lượt bắn chiến thắng",
    ]
    nam=2018
    stt=0
    lichlist=[]
    chitiettranlist=[]
    tranlist=[]
    for j in range (10):#giai dau
        nam+=1
        ngay=random.randint(1,17)
        thang=random.randint(1,12)
        check=True
        tt=0
        for k in range(9):#mon the thao
            ck=1
            bk=2
            tk=4
            tmpngay=ngay
            # tmpthang=thang
            # tmpnam=nam
            vl=random.randint(1,1)
            for i in range(tk+bk+vl+ck): # cac loai vong loai
                if check==True: stt+=1
                matran=f"'TD{tt+1:03d}'"
                tt+=1
                magiaidau=f"'GD{j+1:03d}'"
                sttmonthi=k
                monthidau=montt[sttmonthi]
                timethidau=timelist[sttmonthi]
                thele=f"'{thelethidau[k]}'"
                matbi=f"'TB{random.randint(4*k+1,4*k+4):03d}'"
                if vl>0:
                    vl-=1
                    tentran=tentranlist[3]+" "+monthidau
                    tmpngay+=1
                elif tk>0:
                    tk-=1
                    tentran=tentranlist[2]+" "+monthidau+f" Trận {4-tk}"
                    tmpngay+=1
                elif bk>0:
                    bk-=1
                    tentran=tentranlist[1]+" "+monthidau+f" Trận {2-bk}"
                    tmpngay+=1
                elif ck>0:
                    ck-=1
                    tentran=tentranlist[1]+" "+monthidau
                    tmpngay+=1
                ketqua="Hoàn thành xuất sắc"
                

                tran="("+matran+", "+f"{magiaidau}"+", "+f"'{tentran}'"+", "+f"'{monthidau}'"+", "+str(timethidau)+", "+f"'{ketqua}'),"
                tranlist.append(tran)
                if(check==True):
                    lichstr=lichthidau(stt,nam,thang,tmpngay)
                    lichlist.append(lichstr)
                    malich=f"'LD{stt:03d}'"
                chitiettran=trantosql(matbi,matran,malich,magiaidau,thele)
                chitiettranlist.append(chitiettran)
            check=False
    with open('lich.txt', 'w',encoding='utf-8') as file:
        for l in lichlist:
            file.write(l)
            file.write("\n")    
    with open('chi_tiet_tran.txt', 'w',encoding='utf-8') as file:
        for l in chitiettranlist:
            file.write(l)
            file.write("\n")   

    with open('trandau.txt', 'w',encoding='utf-8') as file:
        for l in tranlist:
            file.write(l)
            file.write("\n") 
def trantosql(matbi,matran,malich,magiaidau,thelethidau):
    return "("+matbi+","+matran+","+malich+","+magiaidau+","+thelethidau+"),"

def lichthidau(stt,nam,thang,ngay):
    from datetime import datetime, timedelta

    # Giới hạn ngày bắt đầu và kết thúc
    start_date = datetime(nam, thang,ngay)

    # In ra ngày ngẫu nhiên
    #return start_date.strftime('%Y,%m,%d,')
    h=[0,30]
    return f"('LD{stt:03d}'"+","+start_date.strftime('%Y,%m,%d,')+\
        str(random.randint(0,23))+","+\
                str(h[random.randint(0,1)])+"),"
# stt=0
# for i in range(500):
#     stt+=1
#     print(f"('LD{stt:03d}'"+lichthidau())


# nhansu_quanly()
# nhansu_hlv()
# nhansu_nhansuquen()
# Vandongvien()
# NhanvienDieuhanh()
Khangia()
# Santhidau()
# Trandau()
# Khangia()
# giave()
# donviThietbi()
# Santhidau()
# trangtbcsvc()
# matbvamasan()
# hopdongchitra()
# chitietchitra()
# chitietdieuhanh()
# chitietthamgiathidau()
# chitiettrandau()
# ve()
# chitietchitra()
