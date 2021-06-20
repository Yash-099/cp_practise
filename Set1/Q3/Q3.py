import numpy as np


## D(i,j) = if A(i)!=B(j) then min(D(i-1,j),D(i,j-1),D(i-1,j-1)) + 1 else min(...)



def min_dist(str1,str2,D10,D01,D00,i,j):
	mini = min(D10,min(D00,D01))
	if str1[i]==str2[j]:
		return mini
	else:
		return (mini + 1)


if __name__ == '__main__':
	str1 = 'editing'
	str2 = 'distance'
	D = np.zeros((len(str1)+1,len(str2)+1))
	for i in range(len(str1)+1):
		D[i,0] = i
	for i in range(len(str2)+1):
		D[0,i] = i

	for i in range(1,len(str1)+1):
		for j in range(1,len(str2)+1):
			D[i,j] = min_dist(str1,str2,D[i-1,j],D[i,j-1],D[i-1,j-1],i-1,j-1)
	print(int(D[len(str1),len(str2)]))