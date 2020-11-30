import datetime
import random

def main(config):  
    random.seed(config["seed"])
    some_date = random_date()
    print(some_date)	
    return some_date
		
def random_date():
    earliest = datetime.date(1910,1,1)
    latest  = datetime.date(2018,1,1)
    delta = latest - earliest
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds    
    random_second = random.randrange(int_delta)
    return earliest + datetime.timedelta(seconds = random_second)
	