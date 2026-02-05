# gán biến students rỗng để chứa toàn bộ dữ liệu của các sinh viên.
students = []
# Khởi tạo vòng lặp.
for i in range(3):
    print(f"--- Nhập thông tin sinh viên {i+1} ---")
    name = input("Tên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    Diem_TB = (toan + ly + hoa) / 3
    students.append((name, Diem_TB)) # đẩy name và Diem_TB vào biến students
#In ra kết quả
print("\n--- Kết quả trung bình ---")
for s in students:
    print(f"Sinh viên: {s[0]} - Điểm TB: {s[1]:.2f}")