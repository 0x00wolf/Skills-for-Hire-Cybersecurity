import time
from sys import exit

def clock():
    try:
        utc_offset = (-time.timezone)
        unix_timestamp = time.time()
        t = time.localtime()
        time_ = time.strftime("%H:%M:%S", t)
        print('\n'*40)
        print(f'current time: {time_}')
        print(f'unix timestamp: {unix_timestamp}')
        time.sleep(0.1)
    except KeyboardInterrupt:
        exit(0)
        

if __name__ == '__main__':
    while True:
        clock()


