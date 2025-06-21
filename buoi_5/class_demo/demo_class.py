# Khai báo class Employee
class Employee:
    def __init__(self, name, department, salary):
        self.name = name 
        self.department = department 
        self.salary = salary 
    
    def get_info(self):
        print(f"{self.name} - {self.department} - ${self.salary}")
    
# Tạo đối tượng và gọi phương thức get_info() 
emp1 = Employee("Alice", "HR", 700)
emp1.get_info() 
# Output: Alice - HR - $700

# Thay đổi thuộc tính
emp1.department = "IT"
emp1.get_info()
# Output: Alice - IT - $700

# Xoá thuộc tính salary 
# del emp1.salary
emp1.get_info()
# Lỗi vì đã mất đi thuộc tính salary