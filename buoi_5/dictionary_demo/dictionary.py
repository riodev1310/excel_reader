employee = {
    "name": "Việt An",
    "department": "Data Science",
    "salary": 700
}

# Truy cập vào tên của employee 
print(employee["name"])

# Thêm cặp key-value mới 
employee["role"] = "Data Scientist" 
print(employee)

# Thay đổi salary thành 1200 
employee["salary"] = 1200
print(employee)

# Xoá một cặp key-value 
# Cách 1: nhanh trực tiếp nhưng sẽ báo lỗi nếu key không tồn tại 
del employee["department"]
# Cách 2: có thể thêm giá trị mặc định nếu key không tồn tại => Tránh được lỗi
employee.pop("department", None) # Không lỗi nếu không có key department
print(employee) 