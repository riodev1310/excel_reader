# List chứa 3 phần tử
ages = [19, 26, 29]
print(ages) 

# Output: [19, 26, 29]

da_skills = ['Excel', 'PowerBI', 'SQL', 'DAX', 'Python']
print("Original List: ", da_skills) 

# Sử dụng phương thức append() 
da_skills.append("Streamlit")

print("Updated List: ", da_skills)


da_skills = ['Excel', 'PowerBI', 'SQL', 'DAX', 'Python']
print("Original List: ", da_skills) 

# Sử dụng phương thức insert() 
da_skills.insert(1, "Pandas")

print("Updated List: ", da_skills)


da_skills = ['Excel', 'PowerBI', 'SQL', 'DAX', 'Python']
print("Original List: ", da_skills) 

# Đổi Python thành Py
da_skills[4] = "Py"

print("Updated List: ", da_skills)


da_skills = ['Excel', 'PowerBI', 'SQL', 'DAX', 'Python']
print("Original List: ", da_skills) 

# Đổi Python thành Py
da_skills.remove('DAX')

print("Updated List: ", da_skills) # Updated Lists: ['Excel', 'PowerBI', 'SQL', 'Python']


da_skills = ['Excel', 'PowerBI', 'SQL', 'DAX', 'Python']
print("Total Elements: ", len(da_skills)) # Total Elements: 5 