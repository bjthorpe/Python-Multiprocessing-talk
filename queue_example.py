import os
import random
import time
from multiprocessing import Process, Queue
from queue import Empty


def hello_sum(input, sum):
    '''   The function is very British and patiently waits its turn in the queue.'''
    total = 0
    output = 0
    proc_id = os.getpid()
# as long as there are numbers in the queue output each number when
# you get it and keep a running total.
    while not input.empty():
        # We have to enclose this in a try/except since we are running asynchronously 
        # and the queue may become empty. between checking and getting the value off the queue. 
        # In which case get() throws an empty exception.
        try:
            output = input.get()
        except Empty:
            pass
            break
        else:
            total = total + output
            print(
                f"Hello there, this is Process: {proc_id}. I took {output} of the queue")
            time.sleep(0.1)
    # when there are no more numbers put final total into the sum queue as a
    # tuple along with process id
    sum.put((proc_id, total))
    print(f"Bye World!!")


if __name__ == '__main__':
    processes = []
    inputs = Queue()
    sum = Queue()
    # put 1000 random numbers in the input queue
    for number in range(100):
        x = random.randint(1,100)
        inputs.put(x)
    for i in range(4):
        # create four processes and pass in the two queues as parameters
        process = Process(target=hello_sum, args=(inputs, sum))
        process.start()
        processes.append(process)
    # As usual wait for the processes to complete
    for process in processes:
        process.join()
# When done extract all sums from the sum queue
    for i in range(sum.qsize()):
        A = sum.get()
        print(A)
    print("Finished")
