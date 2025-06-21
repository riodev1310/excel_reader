from manage_employee import Employee, EmployeeManager

# Tạo nhân viên 
emp1 = Employee("Alice", "HR", 700)
emp2 = Employee("Bob", "IT", 1200)
emp3 = Employee("Charlie", "IT", 1100)
emp4 = Employee("Diana", "HR", 800)
emp5 = Employee("Eve", "Finance", 950)
emp6 = Employee("Frank", "Finance", 1050)

# Thêm nhân viên
emp_list = [emp1, emp2, emp3, emp4, emp5, emp6]

# Tạo đối tượng quản lý 
manager = EmployeeManager(emp_list)  

# Tổng lương
print(f"Tổng lương: {manager.total_salary()}")

# Lọc nhân viên theo phòng ban 
IT_team = manager.filter_by_department("IT") 
print(f"Nhân viên IT Team: {[e.name for e in IT_team]}")

# Nhân viên lương cao 
high_paid = manager.get_high_paid()
print(f"Lương cao: {[e.name for e in high_paid]}") 