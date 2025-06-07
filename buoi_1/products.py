import openpyxl
import os


# Kiểm tra file Excel đã tồn tại chưa
excel_file = "product_information.xlsx"
# if os.path.exists(excel_file):
#     wb = openpyxl.load_workbook(excel_file)
#     ws = wb.active
# else:
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Product Information"
# Tạo header
headers = ["ID sản phẩm", "Tên sản phẩm", "Phí sản xuất", "Phí vận chuyển", 
                   "Tỷ lệ lợi nhuận", "Giá bán sản phẩm"]
ws.append(headers)


# Nhập thông tin sản phẩm
product_id = input("Nhập ID sản phẩm: ").strip()
        
product_name = input("Nhập tên sản phẩm: ").strip()
        
# Nhập và kiểm tra phí sản xuất
production_cost = float(input("Nhập phí sản xuất: "))
shipping_cost = float(input("Nhập phí vận chuyển: "))
                
# Nhập và kiểm tra tỷ lệ lợi nhuận
profit_margin = 0.1
            
# Tính giá bán sản phẩm
selling_price = (production_cost + shipping_cost) / (1 - profit_margin)
        
# Thêm dữ liệu vào worksheet
ws.append([
    product_id,
    product_name,
    production_cost,
    shipping_cost,
    profit_margin,
    round(selling_price, 2)  # Làm tròn giá bán đến 2 chữ số thập phân
])
           
# Lưu file
wb.save(excel_file)
print(f"Dữ liệu đã được lưu vào file {excel_file}")