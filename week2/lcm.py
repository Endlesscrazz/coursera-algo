import sys

a,b = [int(i) for i in input().split()]

def gcd_euclid(a,b):

	dividend = a if(a>=b) else b
	divisor = a if(a<=b) else b

	while divisor != 0:
		remainder = dividend % divisor
		dividend = divisor
		divisor = remainder

	return dividend

def lcm_fast(a,b):
	return(a*b) // gcd_euclid(a,b)

print(lcm_fast(a,b))


