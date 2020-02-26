from multiprocessing import Pool
import os
# square-function to run in parallel
output=0
def sqfunc(x):
    'This function contains an error'
    raise Exception( "can you hear me!!")
    square = x*x
    return square
def err_move(err):
    pid = os.getpid()
    print('Caught exception in process (x = %i):' % pid)
    return err
# The callback function doesn't return anytging so we never get the error
def move(value):
    global output
    output=value
if __name__ == '__main__':
    pool = Pool(processes=4)
    input_list = [1, 2, 3, 4]
    for i in input_list:
        err=pool.apply_async(sqfunc,args=(i,),callback=move)
    pool.close()
    pool.join()
    if err:
        raise err.get()
    print(output) # This value should not be zero
