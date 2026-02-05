# Gán biến yêu cầu người dùng nhập vào nhiệt độ để chạy chương trình.
c = float(input("Nhập độ C: "))
# Thực hiện phép tính chuyển đổi từ độ C sang độ F.
f = c * 9/5 + 32
# In ra kết quả.
print(f"{c} độ C tương đương với {f:.2f} độ F")