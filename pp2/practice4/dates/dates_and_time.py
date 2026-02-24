#Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)
#The following will output the particular info of datatime
print(x.year)
print(x.day)
print(x.strftime("%A")) #this will output the weekday
print(x.strftime("%d")) #this will output the day
print(x.strftime("%M")) #this will output the month
print(x.strftime("%Y")) #this will output the year
print(x.strftime("%X")) #this will output the local version of time
print(x.strftime("%C")) #this will output the century

#Create a date object:
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
