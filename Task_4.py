from datetime import datetime as dtdt
from datetime import timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(person):
    birthday=dtdt.strptime(person["birthday"], "%Y.%m.%d").date()
    current_date=dtdt.now().date()
    
    #change year to current year
    birthday_sel=birthday.replace(year=current_date.year)
    #if selebration is in past change to next year
    if birthday_sel<current_date:
        birthday_sel=birthday.replace(year=(current_date.year+1))
    
    #if selebration on Saturday or Sunday - move to next Monday    
    if birthday_sel.weekday() == 5:
        birthday_sel = (birthday_sel+timedelta(days=2))
    elif birthday_sel.weekday() == 6:
        birthday_sel = (birthday_sel+timedelta(days=1))
    return birthday_sel
    
for person in users:
    string = get_upcoming_birthdays(person).strftime("%Y.%m.%d, %a")
    person["next party"] = string
   
print(users)
    

        
    

