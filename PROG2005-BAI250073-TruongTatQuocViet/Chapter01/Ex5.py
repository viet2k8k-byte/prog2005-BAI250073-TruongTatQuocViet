# Gán biến yêu cầu người dùng nhập dữ liệu để chạy chường trình.
name = input("Nhập Tên Của Bạn : ")
age = int(input("Nhập Tuổi Của Bạn : "))
average_score = float(input("Nhập Số Điểm Trung Bình Của Bạn : "))
# Thực hiện phép tính.
age_next_year = age + 1
doubled_score = average_score * 2
# In ra kết quả và kiểu của dữ liệu.
print(f"Tên: {name}, Kiểu: {type(name)}")
print(f"Tuổi sang năm: {age_next_year}, Kiểu: {type(age)}")
print(f"Điểm nhân đôi: {doubled_score}, Kiểu: {type(average_score)}")
