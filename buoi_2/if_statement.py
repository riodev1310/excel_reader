kpi = 100
result = 150
base_salary = 1000

if result >= kpi:  
    print("You got", base_salary + base_salary * 0.2)
    
    

kpi = 100
min_result = 50
result = 70
base_salary = 1000

if min_result <= result >= kpi:  
    print("You got", base_salary + base_salary * 0.2)
    
if min_result <= result < kpi:  
    print("You got", base_salary)
        
if min_result > result:  
    print("You are fired")
    
    
kpi = 100
result = 70
base_salary = 1000

if result >= kpi:  
    print("You got", base_salary + base_salary * 0.2)
    print("Congratulations! You're unbelievable")
else:  
    print("You got", base_salary)
    print("Put in a bit more effort for a bonus.")
    


kpi = 100
min_result = 50
result = 70
base_salary = 1000


if result >= min_result:
    if result >= kpi:
        print("You got", base_salary + base_salary * 0.2) 
        print("Congratulations! You're unbelievable")
    else:
        print("You got", base_salary)
        print("Put in a bit more effort for a bonus.")
else:
    print("You are fired")
    
    
kpi = 100
min_result = 50
result = 70
base_salary = 1000

if result >= min_result and result >= kpi:
    print("You got", base_salary + base_salary * 0.2) 
    print("Congratulations! You're unbelievable")
elif result < kpi:
    print("You got", base_salary)
    print("Put in a bit more effort for a bonus.")
else:
    print("You are fired")