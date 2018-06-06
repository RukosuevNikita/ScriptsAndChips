#!/usr/bin/env python3

from datetime import datetime
from dateutil import relativedelta


def validate(age, pass_age):
    return not (
        age.years < 14 or
        (
            (20, 1) < (age.years, age.months) < (45, 1) and
            (pass_age.years < 20)
        ) or
        ((age.years, age.months) > (45, 1) and (pass_age.years < 45))
    )


def main():
    print("Input date in format DD.MM.YYYY")
    # Date's input
    birthinput = input('Enter your date of birth: ')
    passinput = input('Enter the date of receipt of your passport: ')
    # Converting input strings into date's to work with
    today = datetime.today()
    birthday = datetime.strptime(birthinput, "%d.%m.%Y")
    passday = datetime.strptime(passinput, "%d.%m.%Y")
    # Calculating actual age and age when passport was getting
    age = relativedelta.relativedelta(today, birthday)
    pass_age = relativedelta.relativedelta(passday, birthday)

    valid = validate(age, pass_age)
    print(valid)


if __name__ == "__main__":
main()
