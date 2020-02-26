from multiprocessing import Pool
import time
def check_prime(num):
    '''Crude Function to check if a number is prime or not and if so return that number'''
   # check for factors
    for i in range(2,num):
        if (num % i) == 0:
            break
    else:
        return num 

def check_in_parallel(data_list):
    # initalise the pool. 
    #Note: Pool takes in the number of proceses in the pool 
    pool = Pool(4)  
    # Here we are using map to apply check_prime over the list using the pool.
    result_list = pool.map_async(check_prime, data_list)
    # Tells the main process to wait until the pool is finished and then close the pool
    # this is needed since assync methods are non-blocking.
    pool.close()
    pool.join()
    #extract the actual results from the AsyncResults object
    primes=result_list.get()
    #remove None from the results
    primes = list(filter(None, primes))
    print(primes)
    #print(start-datetime.now())

if __name__ == '__main__':
    start = time.time()
    data_list=[]
    #create list of numbers from 2 to 100000
    # Note: loop has been created in reverse
    for x in range(2,100000):
    #for x in range(100000,2,-1):
        data_list.append(x)
    #submit list to the pool for processing
    check_in_parallel(data_list)
    end=time.time()
    print(f"Run took {end-start} seconds")
