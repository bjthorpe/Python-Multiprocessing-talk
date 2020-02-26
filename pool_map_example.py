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
    result_list = pool.map(check_prime, data_list)
    # Not stricly nesacary here but it is always good practice to close and join 
    #the pool when you are finished with it (this is more nessecary with assync methods later).
    pool.close()
    pool.join()
    #remove Nones from the results list
    primes = list(filter(None, result_list))
    print(primes)
    #print(start-datetime.now())

if __name__ == '__main__':
    start = time.time()
    data_list=[]
    #create list of numbers from 2 to 100000
    for x in range(2,100000):
        data_list.append(x)
    #submit list to the pool for processing
    check_in_parallel(data_list)
    end=time.time()
    print(f"Run took {end-start} seconds")
