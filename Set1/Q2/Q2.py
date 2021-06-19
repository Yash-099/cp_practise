import numpy as np


## D(i) = min(D(i/2)+1,D(i/3)+1,D(i-1)+1)


if __name__ == '__main__':
	n = 96234
	D = np.zeros(n+1)
	D[1] = 1
	D[2] = 2
	
	for i in range(3,n+1):
		if (i+1) % 2 == 0 and (i+1)%3==0:
			D[i] = min(min(D[int(i/2)],D[int(i/3)]),D[i-1]) + 1
		elif (i+1) % 2 == 0:
			D[i] = min(D[int(i/2)],D[i-1]) + 1
		elif (i+1) % 3 == 0:
			D[i] = min(D[int(i/3)],D[i-1]) + 1
		else :
			D[i] = D[i-1] + 1

	print(int(D[n-1]))