# Gán biến yêu cầu người dùng nhập số để chạy chương trình.
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
# In ra kết quả (Đưa phép tính vào phần này để rút gọn dòng code).
print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}")
print(f"Tích: {a * b}")
#Vì một số không thể chia cho 0 nên dùng if else tránh xảy ra lỗi.
print(f"Thương: {a / b if b != 0 else 'Không thể chia cho 0'}")