from openpyxl import Workbook, load_workbook

# Define excel file to save information
excel_file = "so_yeu_ly_lich.xlsx"

wb = Workbook()
ws = wb.active
ws.title = "User Information"
# Defines headers
headers = [
    "Họ và tên", "Giới tính", "Ngày sinh", "Nơi sinh", "Nguyên quán",
    "Hộ khẩu", "Chỗ ở hiện nay", "Điện thoại", "Dân tộc", "CCCD/CMND",
    "Ngày cấp", "Nơi cấp", "Trình độ văn hóa", "Sở trường"
]
ws.append(headers)

wb.save(excel_file)
print("Excel file 'so_yeu_ly_lich.xlsx' created successfully.")