import openpyxl
import os


# Kiểm tra file Excel đã tồn tại chưa
excel_file = "product_information.xlsx"
if os.path.exists(excel_file):
    wb = openpyxl.load_workbook(excel_file)
    ws = wb.active
else:
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Product Information"
    # Tạo header
    headers = ["ID sản phẩm", "Tên sản phẩm", "Phí sản xuất", "Phí vận chuyển", 
                   "Tỷ lệ lợi nhuận", "Có khuyến mãi", "Giá bán sản phẩm"]
    ws.append(headers)


# Nhập thông tin sản phẩm
product_id = input("Nhập ID sản phẩm: ").strip()
        
product_name = input("Nhập tên sản phẩm: ").strip()
        
# Nhập và kiểm tra phí sản xuất
production_cost = float(input("Nhập phí sản xuất: "))
shipping_cost = float(input("Nhập phí vận chuyển: "))
                
# Nhập và kiểm tra tỷ lệ lợi nhuận
profit_margin = 0.1

# Nhập để phân loại mặt hàng 
discount = int(input("Phân loại mặt hàng: (0: Không có chương trình khuyến mãi nào, 1: Có chương trình khuyến mãi): "))
            
# Tính giá bán sản phẩm
if discount == 0:
    label = "KHÔNG"
    selling_price = (production_cost + shipping_cost) / (1 - profit_margin)
else: 
    label = "Nằm trong chương trình khuyến mãi X"
    voucher = int(input("Nhập % khuyến mãi (ví dụ: 30, 40, ...): ")) / 100
    selling_price = ((production_cost + shipping_cost) / (1 - profit_margin)) * (1 - voucher)
        
# Thêm dữ liệu vào worksheet
ws.append([
    product_id,
    product_name,
    production_cost,
    shipping_cost,
    profit_margin,
    label,
    round(selling_price, 2)  # Làm tròn giá bán đến 2 chữ số thập phân
])
           
# Lưu file
wb.save(excel_file)
print(f"Dữ liệu đã được lưu vào file {excel_file}")