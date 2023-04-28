import multiprocessing
import random
from time import sleep
from datetime import datetime
def currtime(seconds):
    sleep(seconds)
    print(f"waited {seconds:.2f} seconds")
    print('current time is', datetime.utcnow())
    
if __name__ == '__main__':
  
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=currtime, args=(seconds,))
        proc.start()