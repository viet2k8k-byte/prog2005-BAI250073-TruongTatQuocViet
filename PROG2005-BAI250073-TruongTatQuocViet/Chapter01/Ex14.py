#Bước 1 : import thư viện math để sử dụng câu lệnh trong thư viện math
import math
#Bước 2 : Thử nghiệm kèm theo if else để in ra kết quả nếu lỗi sẽ qua bước 3.
try:
    num = float(input("Nhập một số: "))
    if num < 0:
        print("Lỗi: Không thể tính căn bậc hai của số âm.")
    else:
        print(f"Căn bậc hai của {num} là: {math.sqrt(num):.2f}")
#Bước 3 : Thực thi khi người dùng không nhập số mà nhập chữ.
except ValueError:
    print("Lỗi: Vui lòng nhập một số thực.")