import datetime

def date_in_future(integer):
    result = None
    date_now = datetime.datetime.today()
    day = str(date_now.date().day)
    month = str(date_now.date().month)

    if type(integer) == int:
        result = date_now + datetime.timedelta(days=integer)
    else:
        result = date_now

    day = str(result.date().day)
    month = str(result.date().month)

    if len(day) < 2:
        day = "0" + day
    if len(month) < 2:
        month = "0" + month   

    return day + "-" + month + "-" + str(result.date().year) + " " + str(result.time().replace(microsecond=0))
    
print(date_in_future([]))
print(date_in_future(20))

