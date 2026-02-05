n = input("Nhập số nguyên dương có 5 chữ số: ")
if len(n) == 5 and n.isdigit():
    max_digit = max(n)
    print(f"Chữ số lớn nhất là: {max_digit}")
else:
    print("Vui lòng nhập đúng 5 chữ số.")