# Gán biến yêu cầu người dùng nhập dữ liệu để chạy chương trình.
Tuoi_Can_Nhap = int(input("Nhập tuổi của bạn: "))
# Dùng if else để kiểm tra độ hợp lệ và in ra kết quả
if 1 <= Tuoi_Can_Nhap <= 120 :
    print("Tuổi hợp lệ.")
else:
    print("Tuổi không hợp lệ (phải từ 1 đến 120).")