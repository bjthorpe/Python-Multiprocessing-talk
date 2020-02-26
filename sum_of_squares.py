def sum_of_squares(number):
    '''    The function sums the squares of integers from one to whatever number it is provided.'''
    result = 0
    for I in range(number):
        result = result + (I * I)
    return result
	
if __name__ == '__main__':	
	from datetime import datetime
	start = datetime.now()
	number = 100
	result = sum_of_squares(number+1)
	print(f"The sum of the squares for the first {number} integers is {result}")
	print("Function took", datetime.now() - start)