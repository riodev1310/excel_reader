def greet(name):
    message = "Xin chào, " + name + "!"  # Biến cục bộ 'message'
    print(message)

# Gọi hàm
greet("Hùng")

# Thử truy cập biến cục bộ 'message' bên ngoài hàm
try:
    print(message)  # Sẽ gây lỗi vì 'message' không tồn tại ngoài phạm vi hàm
except NameError as e:
    print("Lỗi:", e)  # Kết quả: Lỗi: name 'message' is not defined

# Thử truy cập tham số 'name' bên ngoài hàm
try:
    print(name)  # Sẽ gây lỗi vì 'name' chỉ tồn tại trong phạm vi hàm
except NameError as e:
    print("Lỗi:", e)  # Kết quả: Lỗi: name 'name' is not defined
    
    
def send_notification(customer_name, message): 
    print(f"Gửi thông báo đến {customer_name}: {message}") 

def calculate_profit(revenue, expenses):
    profit = revenue - expenses
    return profit  # Hàm dừng lại ngay sau khi return
    
    
# def calculate_profit(revenue, expenses):
#     profit = revenue - expenses
#     return profit  # Hàm dừng lại ngay sau khi return
#     print("Câu lệnh này sẽ không được thực thi vì nằm sau return")

# Gọi hàm
result = calculate_profit(100, 70)
print("Lợi nhuận:", result)  # Kết quả: Lợi nhuận: 30


# Ví dụ hàm có nhiều điều kiện với return
def check_profit(profit):
    if profit > 0:
        return "Có lời"  # Thoát hàm ngay sau return
    elif profit < 0:
        return "Bị lỗ"    # Thoát hàm ngay sau return
    return "Hoà vốn"         # Nếu không thỏa mãn điều kiện trên, trả về "Hoà vốn"


def is_kpi_achieved(actual_value, kpi):
    if actual_value > kpi: 
        return True 
    else:
        return False 