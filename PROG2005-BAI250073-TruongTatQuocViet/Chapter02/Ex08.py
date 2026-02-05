n = int(input("Nhập một số dương: "))
so_dao = 0
while n > 0:
    chu_so_cuoi = n % 10
    so_dao = so_dao * 10 + chu_so_cuoi
    n //= 10
print(f"Số đảo ngược là: {so_dao}")