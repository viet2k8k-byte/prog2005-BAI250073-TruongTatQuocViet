# Gán biến yêu cầu người dùng nhập dữ liệu để chạy chương trình.
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))
# Gán biến "bmi" trong biến tính toán chỉ số khối cơ thể.
bmi = weight / (height ** 2)
# In ra kết quả dùng sau dấu "." 2 số.
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")