# Gán biến yêu cầu người dùng nhập dữ liệu để chạy chương trình.
n = int(input("Nhập Số : "))
# Định nghĩa để hàm thực hiện phép tính.
def is_even(n):
    return n % 2 == 0
# In ra kết quả.
print(f"Số {n} có là số chẵn không ?\n{is_even(n)}")