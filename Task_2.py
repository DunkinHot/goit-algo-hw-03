import random
#input range and number of instances
min=1
max=49
quantity=6

def get_numbers_ticket(min, max, quantity):
    if (max-min)<(quantity-1) or min>max or max>1000:
        return "Invalid input values"
    try:
        list=[]
        while len(list)<quantity:
            a=random.randint(min,max)
            if a not in list:
                list.append(a)
        return(sorted(list))
    except:
        return "Error input value"
    
print(f"WINNING NUMBERS: {get_numbers_ticket(min, max, quantity)}")