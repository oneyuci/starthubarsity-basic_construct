def conditional_func(param):
    
    value1 = 5
    if value1 == param or value1 < 10:  
        print("Truthy")
    
    else:
        print("Falsy")



conditional_func(5)