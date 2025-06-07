import openpyxl
import os

def calculate_selling_price(production_cost, shipping_cost, profit_margin):
    return (production_cost + shipping_cost) / (1 - profit_margin)

def main():
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
                   "Tỷ lệ lợi nhuận", "Giá bán sản phẩm"]
        ws.append(headers)

    while True:
        # Nhập thông tin sản phẩm
        product_id = input("Nhập ID sản phẩm: ").strip()
        
        product_name = input("Nhập tên sản phẩm: ").strip()
        
        # Nhập và kiểm tra phí sản xuất
        while True:
            try:
                production_cost = float(input("Nhập phí sản xuất: "))
                if production_cost < 0:
                    print("Phí sản xuất không thể âm! Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ cho phí sản xuất!")
        
        # Nhập và kiểm tra phí vận chuyển
        while True:
            try:
                shipping_cost = float(input("Nhập phí vận chuyển: "))
                if shipping_cost < 0:
                    print("Phí vận chuyển không thể âm! Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ cho phí vận chuyển!")
        
        # Nhập và kiểm tra tỷ lệ lợi nhuận
        while True:
            try:
                profit_margin = float(input("Nhập tỷ lệ lợi nhuận (0 đến 1): "))
                if not 0 <= profit_margin < 1:
                    print("Tỷ lệ lợi nhuận phải từ 0 đến dưới 1! Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Vui lòng nhập một số hợp lệ cho tỷ lệ lợi nhuận!")
        
        # Tính giá bán sản phẩm
        selling_price = calculate_selling_price(production_cost, shipping_cost, profit_margin)
        
        # Thêm dữ liệu vào worksheet
        ws.append([
            product_id,
            product_name,
            production_cost,
            shipping_cost,
            profit_margin,
            round(selling_price, 2)  # Làm tròn giá bán đến 2 chữ số thập phân
        ])
        
        # Hỏi tiếp tục
        cont = input("Tiếp tục nhập thông tin? (y/n): ").lower()
        if cont != 'y':
            break
    
    # Lưu file
    wb.save(excel_file)
    print(f"Dữ liệu đã được lưu vào file {excel_file}")

if __name__ == "__main__":
    main()