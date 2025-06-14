import openpyxl
from datetime import datetime
import re

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r'^\d{10,11}$'
    return bool(re.match(pattern, phone))

def get_status_code(age, job, is_student):
    if is_student:
        return 1
    if age >= 18:
        return 3 if job else 2
    return None

def main():
    # Tạo workbook và worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "User Information"
    
    # Tạo header
    headers = ["Họ và tên", "Ngày sinh", "Email", "Số điện thoại", "Công việc", 
               "Tình trạng hôn nhân", "Trạng thái tuổi", "Mã trạng thái"]
    ws.append(headers)
    
    while True:
        # Nhập thông tin người dùng
        name = input("Nhập họ và tên: ").strip()
        
        # Nhập và kiểm tra ngày sinh
        while True:
            try:
                birth_date = input("Nhập ngày sinh (dd/mm/yyyy): ")
                birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
                break
            except ValueError:
                print("Định dạng ngày sinh không hợp lệ! Vui lòng nhập lại (dd/mm/yyyy).")
        
        # Tính tuổi và trạng thái tuổi
        age = calculate_age(birth_date)
        age_status = "Trên 18 tuổi" if age >= 18 else "Dưới 18 tuổi"
        
        # Nhập và kiểm tra email
        while True:
            email = input("Nhập email: ").strip()
            if validate_email(email):
                break
            print("Email không hợp lệ! Vui lòng nhập lại.")
        
        # Nhập và kiểm tra số điện thoại
        while True:
            phone = input("Nhập số điện thoại: ").strip()
            if validate_phone(phone):
                break
            print("Số điện thoại không hợp lệ! Vui lòng nhập 10-11 số.")
        
        # Nhập công việc
        job = input("Nhập công việc (để trống nếu chưa có việc làm): ").strip()
        
        # Nhập tình trạng hôn nhân
        while True:
            marital_status = input("Tình trạng hôn nhân (1: Đã có gia đình, 0: Độc thân): ")
            if marital_status in ["0", "1"]:
                marital_status = "Đã có gia đình" if marital_status == "1" else "Độc thân"
                break
            print("Vui lòng nhập 0 hoặc 1!")
        
        # Kiểm tra học sinh/sinh viên
        is_student = False
        if age < 18 or (age >= 18 and not job):
            student_input = input("Bạn có phải là học sinh/sinh viên không? (y/n): ").lower()
            is_student = student_input == 'y'
        
        # Tính mã trạng thái
        status_code = get_status_code(age, job, is_student)
        
        # Thêm dữ liệu vào worksheet
        ws.append([
            name,
            birth_date.strftime("%d/%m/%Y"),
            email,
            phone,
            job,
            marital_status,
            age_status,
            status_code
        ])
        
        # Hỏi tiếp tục
        cont = input("Tiếp tục nhập thông tin? (y/n): ").lower()
        if cont != 'y':
            break
    
    # Lưu file
    wb.save("user_information.xlsx")
    print("Dữ liệu đã được lưu vào file user_information.xlsx")

if __name__ == "__main__":
    main()