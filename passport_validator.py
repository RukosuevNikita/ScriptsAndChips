from datetime import datetime,date

#Description
print('All date are entered in format DD.MM.YYYY')

#Input date's
birthinput = input('Enter your date of birth: ')
receiptinput = input('Enter the date of receipt of your passport: ')
#parse date in format DD.MM.YYYY
birthdate = datetime.strptime(birthinput,"%d.%m.%Y")
passdate = datetime.strptime(receiptinput,"%d.%m.%Y")
#Algorithm


#Output
