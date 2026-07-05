import calendar 
from datetime import date

#For todays date
todays_date = date.today()


#For Calendar of current year
def calendar_main():
    return calendar.calendar(todays_date.year)
