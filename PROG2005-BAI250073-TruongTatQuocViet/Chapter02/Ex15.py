n = int(input("Nhập số nguyên dương: "))
tong = 0
temp = n
while temp > 0:
    tong += temp % 10
    temp //= 10
print(f"Tổng các chữ số của {n} là: {tong}")