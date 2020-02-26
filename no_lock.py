import time
def add_5000_no_lock(total):
	'''This function adds 5000 to the shared value total. 
	The time.sleep functions have been added to make the 
	race condition happen more reliably.'''
	for i in range(1000):
		time.sleep(0.001)
		total.value += 5

def sub_5000_no_lock(total):
	'''This function adds 5000 from the shared value total.
	The time.sleep functions have been added to make the 
	race condition happen more reliably.'''
	for i in range(1000):
		time.sleep(0.001)
		total.value -= 5
		
if __name__ == '__main__':
	# Run this block a few times to see what happens.
	from multiprocessing import Process, Value
	total = Value('i', 300)
	add_proc = Process(target=add_5000_no_lock, args=(total,))
	sub_proc = Process(target=sub_5000_no_lock, args=(total,))

	add_proc.start()
	sub_proc.start()

	add_proc.join()
	sub_proc.join()
	print(total.value)