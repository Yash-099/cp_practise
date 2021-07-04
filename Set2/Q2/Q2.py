import numpy as np



def max_weight(values,w,W,n):
	for i in range(1,n+1):
		for j in range(1,W+1):
			values[i,j] = values[i-1,j]
			if j >= w[i-1]:
				# print(w[i-1])
				if values[i,j]<(values[i-1,j-int(w[i-1])] + w[i-1]) and (values[i-1,j-int(w[i-1])] + w[i-1]) <= W:
					values[i,j] = values[i-1,j-int(w[i-1])] + w[i-1]
	return values[n,W],values


def which_used(values,w):
	where = np.where(values == 2*np.sum(w)//3)
	listt = []
	for i in range(where[0].shape[0]):
		index = [where[0][i],where[1][i]]
		sub_list = []
		for j in range(index[0]):
			if values[index[0]-j,index[1]] == values[index[0]-j-1,index[1]]:
				continue
			else:
				sub_list.append(index[0]-j-1)
				index[1] = index[1] - w[index[0]-j-1]
		listt.append(sub_list)
	return listt

def is_possible(w):
	values = np.zeros((w.shape[0]+1,2*np.sum(w)//3+1))
	max_value,values = max_weight(values,w,2*np.sum(w)//3,w.shape[0])
	# print(max_value,2*np.sum(w)//3,np.sum(w))
	# print(values)
	if max_value != 2*np.sum(w)//3:
		return '0'
	listt = which_used(values,w)
	# print(listt)
	for i in range(len(listt)):
		new_w = []
		for j in range(len(listt[i])):
			new_w.append(w[listt[i][j]])
		# print(w)
		# print(new_w)
		max_value,values = max_weight(values,new_w,np.sum(new_w)//2,len(new_w))
		if max_value == np.sum(new_w)//2:
			return '1'

	return '0'


if __name__ == '__main__':
	n = int(input())
	w = np.array((input().split(' '))).astype(int)

	if np.sum(w) % 3 !=0:
		print('0')
	elif n<3:
		print('0')
	else:
		print(is_possible(w))