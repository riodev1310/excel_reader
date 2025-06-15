def bubble_sort(list_num):
    n = len(list_num)
    for i in range(n):
        swap = False 
        for j in range(n - i - 1):
            if list_num[j] > list_num[j + 1]:
                swap = True 
                list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j] 
        if swap == False:
            return list_num 
    
