# import time
# import datetime

# print(datetime.datetime.now())

import datetime

x = datetime.datetime(2002,5,7,1,2,3,1234)

print(x)
print(x.strftime("%y"))
print(x.strftime("%m"))
print(x.strftime("%d"))
print(x.strftime("%H"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%f"))
print(x.strftime("%A"))



print(str(x.strftime("%y"))+'/'+str(x.strftime("%m"))+'/'+str(x.strftime("%d"))+','+str(x.strftime("%H"))+':'+str(x.strftime("%M"))+':'+str(x.strftime("%S"))+'.'+str(x.strftime("%f")))

