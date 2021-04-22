import datetime  
from datetime import date 
import calendar

def fun(x):
    daysDictionary = {'Mon':0, 'Tue':0, 'Wed':0,'Thu':0, 'Fri':0,'Sat':0, 'Sun':0}
    for j in x:
        date = j
        year,month,day = (int(i) for i in date.split('-'))
        dayNumber = calendar.weekday(year, month, day) 
        days =['Mon', 'Tue', 'Wed', 'Thu','Fri', 'Sat', 'Sun']
        daysDictionary[days[dayNumber]]+=x[j]
        print(daysDictionary[days[dayNumber]])
    print(daysDictionary)

x = {'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}
fun(x)
