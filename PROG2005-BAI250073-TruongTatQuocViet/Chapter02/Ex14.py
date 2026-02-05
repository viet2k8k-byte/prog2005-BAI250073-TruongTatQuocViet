n = int(input("Nhập n: "))
if n < 2:
    check = False
else:
    check = True
    for i in range(2, n):
        if n % i == 0:
            check = False
            break
print(f"{n} là số nguyên tố" if check else f"{n} không là số nguyên tố")