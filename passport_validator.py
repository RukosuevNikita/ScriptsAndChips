from datetime import datetime,date

#Description
print('All date are entered in format DD.MM.YYYY')

#Input date's
birthinput = input('Enter your date of birth: ')
receiptinput = input('Enter the date of receipt of your passport: ')
#parse date in format DD.MM.YYYY
birthdate = datetime.strptime(birthinput,"%d.%m.%Y")
passdate = datetime.strptime(receiptinput,"%d.%m.%Y")
#subtraction years and month from birthday to passport receiving
age = passdate.year - birthdate.year
months = passdate.month - birthdate.month
#Algorithm
def main(age,months):
    if age >= 14 and months >= 1:
        print('Yes')
    elif age >= 20 and months <= 0:
        print('No')
    elif age >= 20 and months >= 1:
        print('Yes')
    elif age >= 40 and months <= 0:
        print('No')
    elif age >= 40 and months >= 1:
        print('Yes')
    else:
        print('No')



#Output
if __name__ == '__main__':
    main(age,months)
