import openpyxl
from datetime import datetime
import re
import os

# def calculate_age(birth_date):
#     today = datetime.today()
#     age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return age

# def get_status_code(age, job):
#     if age <= 18 or job == "sinh viên":
#         return 1
#     elif age >= 18:
#         return 3 if job else 2
#     return None


excel_file = "user_information.xlsx"
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "User Information"
# Tạo header nếu file mới
headers = ["Họ và tên", "Ngày sinh", "Email", "Số điện thoại", "Công việc", 
            "Tình trạng hôn nhân"]
ws.append(headers)
    
    
# Nhập thông tin người dùng
name = input("Nhập họ và tên: ").strip()
        
# Nhập và kiểm tra ngày sinh
birth_date = input("Nhập ngày sinh (dd/mm/yyyy): ")
birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        
# Tính tuổi và trạng thái tuổi
# age = calculate_age(birth_date)
# age_status = "Trên 18 tuổi" if age >= 18 else "Dưới 18 tuổi"
        
# Nhập và kiểm tra email
email = input("Nhập email: ").strip()
        
phone = input("Nhập số điện thoại: ").strip()
        
# Nhập công việc
job = input("Nhập công việc (để trống nếu chưa có việc làm): ").strip()
        
# Nhập tình trạng hôn nhân
marital_status = int(input("Tình trạng hôn nhân (1: Đã có gia đình, 0: Độc thân): "))
        
# Tính mã trạng thái
# status_code = get_status_code(age, job.lower())
        
# Thêm dữ liệu vào worksheet
ws.append([
    name,
    birth_date.strftime("%d/%m/%Y"),
    email,
    phone,
    job,
    marital_status,
])
        
# Lưu file
wb.save("user_information.xlsx")
print("Dữ liệu đã được lưu vào file user_information.xlsx")