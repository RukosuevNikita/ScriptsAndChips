#!/usr/bin/env python3
from datetime import datetime,date
from dateutil import relativedelta

birthinput = input('Enter your date of birth: ')
passinput = input('Enter the date of receipt of your passport: ')


today = datetime.today()
birthday = datetime.strptime(birthinput,"%d.%m.%Y")
passday = datetime.strptime(passinput,"%d.%m.%Y")

age = relativedelta.relativedelta(today,birthday)
pass_age = relativedelta.relativedelta(passday,birthday)

def difference(today,age,pass_age):
        if age.years < 14:
                return False



        else:
                return True

if __name__ == "__main__":
        difference(today,age,pass_age)
