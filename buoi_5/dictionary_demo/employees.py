employees = [
    {"name": "Alice", "department": "HR", "salary": 700},
    {"name": "Bob", "department": "IT", "salary": 1200},
    {"name": "Charlie", "department": "IT", "salary": 1100},
    {"name": "Diana", "department": "HR", "salary": 800},
    {"name": "Eve", "department": "Finance", "salary": 950},
    {"name": "Frank", "department": "Finance", "salary": 1050} 
]

# 1. Tính tổng lương theo phòng ban
salary_by_dept = {} 
# Key: lưu tên phòng ban
# Value: lưu tổng lương của phòng ban đó

for emp in employees: 
    dept = emp["department"]
    salary = emp["salary"]
    if dept not in salary_by_dept:
        salary_by_dept[dept] = salary 
    else:
        salary_by_dept[dept] += salary 

print(f"Tổng lương theo phòng ban: {salary_by_dept}") 


# 2. Đếm số nhân viên theo phòng ban 
count_by_dept = {} 
# Key: lưu tên phòng ban 
# Value: tổng số nhân viên của phòng ban đó
for emp in employees: 
    dept = emp["department"]
    count_by_dept[dept] = count_by_dept.get(dept, 0) + 1 
    
print(f"Tổng số nhân viên theo phòng ban: {count_by_dept}") 


# 3 Gom nhóm tên nhân viên theo phòng ban (dictionary of list) 
group_by_dept = {}
# Key: tên phòng ban 
# Value: một list chứa tên các nhân viên 

for emp in employees:
    dept = emp["department"]
    name = emp["name"] 
    group_by_dept.setdefault(dept, []).append(name) 

print(f"Nhân viên theo phòng ban: {count_by_dept}") 