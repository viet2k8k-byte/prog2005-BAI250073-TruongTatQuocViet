# Gán biến yêu cầu người dùng nhập số để chạy chương trình.
a = int(input("Nhập Số : "))
b = int(input("Nhập Số : "))
# Định nghĩa để hàm  thực hiện phép tính.
def sum_two_numbers(a, b):
    return a + b
# Gán biến cho hàm thực hiện phép tính.
result = sum_two_numbers(a, b)
# In ra kết quả.
print(f"Kết quả hàm sum_two_numbers: {result}")