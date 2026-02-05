# Gán biến yêu cầu người dùng nhập dữ liệu để chạy chường trình.
text = input("Nhập một chuỗi : ")
# Gán biến Dem trong biến sẽ tính toán số lần xuất hiện "a" trong chuỗi
Dem = text.lower().count('a')
# In ra kết quả.
print(f"Ký tự 'a' xuất hiện {Dem} lần.")