import os
from multiprocessing import Process
def hello_world(input):
    '''   The function just popped up to say hello and now its gone back down below.'''
    # We can use the OS module in Python to print out the process ID
    # assigned to the call of this function.
    proc_id = os.getpid()
    print(f"Hello there, this is Process: {proc_id}. My input variable is {input}")
    print(f"Bye World!!")

if __name__ == '__main__':
    processes=[]
    for number in range(10):
# Processes are spawned by creating a Process object and
# then calling its start() method.
        process = Process(target=hello_world, args=(number,))
        process.start()
        processes.append(process)
# We invoke join on each process to tell the main processes to wait for all the others to complete
# before continuing.
    for process in processes:
        process.join()
    print("Finished")
        
