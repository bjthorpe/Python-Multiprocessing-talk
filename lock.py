# First we need to import Lock and then we can re-write our functions to use the lock
from multiprocessing import Process, Lock, Value
import time
def add_5000_lock(total, lock):
	'''This function adds 5000 to the shared value total.
	Even with the time.sleep functions the race condition
	should not occur because of the lock.'''
	for i in range(1000):
		time.sleep(0.001)
		lock.acquire()
		# This line is only run by one process at a time
		total.value += 5
		lock.release()
		
def sub_5000_lock(total, lock):
	'''This function subtracts 5000 from the shared value total.
	Even with the time.sleep functions the race condition
	should not occur because of the lock.'''
	for i in range(1000):
		time.sleep(0.001)
		lock.acquire()
		# This line is only run by one process at a time
		total.value -= 5
		lock.release()
		
if __name__ == '__main__':
	total = Value('i', 300)
	lock = Lock()
	# We then need to define a lock object and pass it into each process
	add_proc = Process(target=add_5000_lock, args=(total, lock))
	sub_proc = Process(target=sub_5000_lock, args=(total, lock))

	add_proc.start()
	sub_proc.start()
	
	add_proc.join()
	sub_proc.join()
	print(total.value)