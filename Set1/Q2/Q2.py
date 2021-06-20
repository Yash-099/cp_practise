import numpy as np


## D(i) = min(D(i/2)+1,D(i/3)+1,D(i-1)+1)


if __name__ == '__main__':
	n = 10000000
	listt = []
	listt.append('')
	listt.append('1 ')
	listt.append('1 2 ')
	D = np.zeros(n+1)
	D[1] = 0
	D[2] = 1
	
	for i in range(3,n+1):
		if (i) % 2 == 0 and (i)%3==0:
			D[i] = min(min(D[int(i/2)],D[int(i/3)]),D[i-1]) + 1
			if D[i]==D[int(i/2)]+1:
				listt.append(listt[int(i/2)]+str(i) + ' ')
			elif D[i]==D[int(i/3)]+1:
				listt.append(listt[int(i/3)]+str(i) + ' ')
			elif D[i]==D[i-1]+1:
				listt.append(listt[i-1]+str(i) + ' ')
		elif (i) % 2 == 0:
			D[i] = min(D[int(i/2)],D[i-1]) + 1
			if D[i]==D[int(i/2)]+1:
				listt.append(listt[int(i/2)]+str(i) + ' ')
			elif D[i]==D[i-1]+1:
				listt.append(listt[i-1]+str(i) + ' ')
		elif (i) % 3 == 0:
			D[i] = min(D[int(i/3)],D[i-1]) + 1
			if D[i]==D[int(i/3)]+1:
				listt.append(listt[int(i/3)]+str(i) + ' ')
			elif D[i]==D[i-1]+1:
				listt.append(listt[i-1]+str(i) + ' ')
		else :
			D[i] = D[i-1] + 1
			listt.append(listt[i-1]+str(i) + ' ')

	print(int(D[n]))
	print(listt[len(listt)-1])