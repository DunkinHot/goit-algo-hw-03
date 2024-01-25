import re

raw_numbers = ["    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   ","  54234"]


def normalize_phone(phone_number):
    pat="[\d\+]+"
    phone_number=''.join(re.findall(pat,number))
    if len(phone_number)<10:
        phone_number="INVALID NUMBER"
    elif len(phone_number)==10:
        phone_number='+38' + phone_number
    elif len(phone_number)==12:
        phone_number='+' + phone_number

    return phone_number


clean_numerbs=[]
for number in raw_numbers:
    clean_numerbs.append(normalize_phone(number))

print(clean_numerbs)

