# Gán biến yêu cầu người dùng nhập dữ liệu để chạy chương trình .
nums = [int(input(f"Nhập số thứ {i+1}: ")) for i in range(3)]
# In ra kết quả.
print(f"Số lớn nhất là: {max(nums)}")