#from datetime import datetime
#dt_now =  datetime.now()


#from datetime import date, timedelta
#dt =dt_now
#delta = timedelta(days=1)

#dt = dt - delta

#dt =dt_now
#delta = timedelta(days=30)
#dt = dt - delta
#print(dt)

from datetime import datetime
dt_2 = datetime(1, 1, 25, 12, 10, 3, 234567)
dt_2.strftime("%d/%m/%Y %H:%m:%S.%f")
print(dt_2)