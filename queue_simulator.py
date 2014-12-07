#! /usr/bin/env python

import random
import math
import sys

def simulate(lam, mu, n, T):
	t = 0
	N = 0
	Xt = -1
	final_array = []
	if (n != 0):
		Xt = n
	while(True):
		U1 = random.random() #arrival time
		U2 = random.random() #departure time
		ta = t + (-1/lam)*math.log(U1)
		td = t + (-1/mu)*math.log(U2)
		if ((ta > td) and (Xt >= 0)):
			if td > T:
				return final_array
			else:
				N=N+1
				t=td
				Xt=Xt-1
				final_array.append((t, -1))
		else:
			if ta > T:
				return final_array
			else:
				N=N+1
				t=ta
				Xt=Xt+1
				final_array.append((t, +1))

def main():
	if (len(sys.argv) < 4):
		print 'Wrong number of input arguments.'
		print 'Usage: python simulate.py <lambda> <mu> <n> <T>'
		exit(0)
	lam=int(sys.argv[1])
	mu=int(sys.argv[2])
	n=int(sys.argv[3])
	T=int(sys.argv[4])
	xt_array=[]
	for i in range(0,999):
		sum = 0
		final_array = simulate(lam,mu,n,T)
		for item in final_array:
			sum = sum + item[1]
			#print '%f, %i'%(item[0],item[1])
		xt_array.append(sum)
	
	open('output.csv','w').close()
	f = open('output.csv', 'w')
	for item in xt_array:
		f.write(str(item)+'\n')
	f.close()



if __name__ == "__main__":
	main()