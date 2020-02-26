from multiprocessing import Pool
# square-function to run in parallel
output=0
def sqfunc(x):
    'This function contains an error'
    raise Exception( "can you hear me!!")
    square = x*x
    return square
# The callback function doesn't return anything so we never get the error
def move(value):
    global output
    output=value
if __name__ == '__main__':
    pool = Pool(processes=4)
    input_list = [1, 2, 3, 4]
    for i in input_list:
        pool.apply_async(sqfunc,args=(i,),callback=move)
    pool.close()
    pool.join()
    print(output) # This value should not be zero
