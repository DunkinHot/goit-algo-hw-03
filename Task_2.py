import random
#input range and number of instances
min=1
max=49
quantity=5

def get_numbers_ticket(min, max, quantity):
    try:
        if (max-min)<(quantity-1) or min>max or max>1000:
            print("Invalid input values")
            return
        list=[]
        while len(list)<quantity:
            a=random.randint(min,max)
            if a not in list:
                list.append(a)
        return(sorted(list))
    except:
        print("Error input value")
        return
    
print(f"WINNING NUMBERS: {get_numbers_ticket(min, max, quantity)}")