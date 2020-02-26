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
	# FYI this is the 29 millionth prime number
	number=533000401
	check_prime(number)