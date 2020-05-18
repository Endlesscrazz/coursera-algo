import sys

a, b = [int(i) for i in input().split()]

def euclid(a,b):

	dividend = a if(a>=b) else b
	divisor = a if(a<=b) else b

	while divisor != 0:

		remainder = dividend % divisor
		dividend = divisor
		divisor = remainder

	return dividend



print(euclid(a,b))