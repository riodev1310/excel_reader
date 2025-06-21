class Employee:
    def __init__(self, name, department, salary):
        self.name = name 
        self.department = department 
        self.salary = salary 
        
    def is_high_paid(self, threshold=1000):
        return self.salary > threshold 
    

class EmployeeManager:
    def __init__(self, emp_list):
        # Khởi tạo list lưu các đối tượng của class Employee
        self.employees = emp_list 
    
    # Thêm nhân viên mới vào hệ thống
    def add_employee(self, emp):
        self.employees.append(emp) 
    
    # Tính tổng lương nhân viên
    def total_salary(self):
        return sum(emp.salary for emp in self.employees) 
    
    # Lấy ra nhân viên của một phòng ban (dept_name)
    def filter_by_department(self, dept_name):
        return [emp for emp in self.employees if emp.department == dept_name] 
    
    # Lấy ra tất cả nhân viên được trả lương cao
    def get_high_paid(self, threshold=1000):
        return [emp for emp in self.employees if emp.is_high_paid(threshold)]