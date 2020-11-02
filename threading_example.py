import time
import threading

startTime = time.time()
number_range = list((x for x in range(2,70000)))
prime_nums = []
for element in number_range:
    for i in range(2, element//2):
        if element % i == 0:
            break
    else:
        prime_nums.append(element)
print(prime_nums)
print('Time taken:', time.time() - startTime)

'''import time
import threading
from queue import Queue

startTime = time.time()
prime_nums = []
def get_primes(number):
    # number_range = list((x for x in range(2,50000)))

    for i in range(2, number//2):
        if number % i == 0:
            break
    else:
        prime_nums.append(number)

def threader():
   while True:
      
      worker = q.get()
      get_primes(worker)
      q.task_done()

q = Queue()
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 70000):
   q.put(worker)
q.join()

print(prime_nums)
print('Time taken:', time.time() - startTime)
'''