n = int(input("Nhập một số: "))
temp = abs(n) # Lấy giá trị tuyệt đối để xử lý cả số âm
tong = 0
while temp > 0:
    tong += temp % 10  # Lấy chữ số cuối cùng
    temp //= 10        # Bỏ chữ số cuối cùng
print(f"Tổng các chữ số là: {tong}")