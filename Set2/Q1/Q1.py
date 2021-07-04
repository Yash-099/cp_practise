import numpy as np



def max_weight(values,w,W,n):
	for i in range(1,n+1):
		for j in range(1,W+1):
			values[i,j] = values[i-1,j]
			if j >= w[i-1]:
				# print(w[i-1])
				if values[i,j]<(values[i-1,j-int(w[i-1])] + w[i-1]):
					values[i,j] = values[i-1,j-int(w[i-1])] + w[i-1]
	return values[n,W]

if __name__ == '__main__':
	W,n = np.array(input().split(' ')).astype(int)
	# W = 10
	# n = 3
	w = np.zeros(n)
	w = np.array(input().split(' ')).astype(int)
	# w[0] = int(1)
	# w[1] = int(4)
	# w[2] = int(8)

	values = np.zeros((n+1,W+1))

	final_value = max_weight(values,w,W,n)

	print(int(final_value))