
import datetime
# _______________________________________TASK No 1______________________________________
#input date
date = "2020-10-09"
from datetime import datetime as dtdt
def get_days_from_today(date):
    today = dtdt.now().date()
    date_object = dtdt.strptime(date, '%Y-%m-%d').date()
    return (today - date_object).days
print(f"The difference is {get_days_from_today(date)} day(s)")