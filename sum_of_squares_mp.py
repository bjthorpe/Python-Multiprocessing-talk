import os
def sum_of_squares_mp(start,stop):
	'''   The function sums the squares of integers between start and stop.'''
	result = 0
	for I in range(start,stop+1):
		result = result + (I * I)
    # We can use the OS module in Python to print out the process ID
    # assigned to the call of this function.
	proc_id = os.getpid()
    print(f"Hello this is Process: {proc_id}. The sum of the squares between {start} and {stop} is {result}")
	
import time
proc_start = time.time()
if __name__ ==  '__main__':
    processes=[]
    # We divide the range into four proceses caculating 1 to 25, 26 to 50, 51 to 75 and 76 to 100 
    start = [1,26,51,76]
    stop = [25,50,75,100]
    # Loop through the list of numbers and create a process
    # to call a function for each item in the list.
    for i,number in enumerate(start):
        # Processes are spawned by creating a Process object and
        # then calling its start() method.
        process = Process(target=sum_of_squares_mp, args=(number,stop[i]))
        process.start()
        processes.append(process)
    
    # We invoke join on each process to tell it to wait for all other processes to complete
    # before continuing.
    for process in processes:
        process.join()

    print(f"Function took {(time.time() - proc_start)*1000} milliseconds")
