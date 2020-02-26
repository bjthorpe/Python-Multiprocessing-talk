# The new version of this function takes in and updates a shared value total
import os
def sum_of_squares_total(total,start,stop):
	''' The function sums the squares of integers from start to stop and adds it to a running total.'''
	result = 0
	for I in range(start,stop+1):
		result = result + (I * I)
	total.value = total.value + result
    # We can use the OS module in Python to print out the process ID
    # assigned to the call of this function.
	proc_id = os.getpid()
	print(f"Hello this is Process: {proc_id}. The sum of the squares between {start} and {stop} is {result}")

if __name__ == '__main__':
	from datetime import datetime
	# Note the added an import for Value
	from multiprocessing import Process, Value
	proc_start = datetime.now()
	processes=[]
	# We define total as a value object (with an initial value of 0) 
	# which is shared between processes.
	total = Value('i', 0)
	# We divide the range into four proceses caculating 1 to 25, 26 to 50, 51 to 75 and 76 to 100 
	start = [1,26,51,76]
	stop = [25,50,75,100]

	# Loop through the list of numbers and create a process
	# calling a function for each item in the list.
	for i,number in enumerate(start):
		# Processes are spawned by creating a Process object and
		# then calling its start() method.
		process = Process(target=sum_of_squares_total, args=(total,number,stop[i]))
		process.start()
		processes.append(process)
    
	# Wait for Python processes to end before continuing.	
	for process in processes:
		process.join()
	# We now need to extract the integer total from the value object
	print(f"Grand total: {total.value}")
	print("process took", datetime.now() - proc_start)