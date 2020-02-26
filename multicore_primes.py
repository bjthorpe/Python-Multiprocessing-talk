# WARNING this code is for demo purposes only and will take a long time to complete
def check_prime(num):
    '''Crude Function to check if a number is prime or not'''
   # check for factors
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number") 

if __name__ == '__main__':
	from multiprocessing import Process
	processes=[]
#check eight large numbers which are a mix of primes and non-primes
	numbers=[1387641293,1111131111,123465969,23659864697,512927377,533000389,452930477,472882027]
	for number in numbers:
		process = Process(target=check_prime, args=(number,))
		process.start()
		processes.append(process)

	for process in processes:
		process.join()
	print("Finished")