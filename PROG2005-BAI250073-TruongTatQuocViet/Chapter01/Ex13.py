# Thử nghiệm nguy cơ xảy ra lỗi ở các dòng code nếu không có lỗi sẽ in ra kết quả nếu có lỗi sẽ tùy thuộc vào lỗi mà sẽ in ra #1 hoặc #2.
try:
    n1 = int(input("Nhập số bị chia: "))
    n2 = int(input("Nhập số chia: "))
    print(f"Kết quả: {n1 / n2:.2f}")
#1 : Bắt lỗi khi người nhập số chia là 0.
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho số 0!")
#2 : Bắt lỗi khi người dùng nhập chữ cái thay vì số.
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")