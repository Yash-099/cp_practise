import numpy as np

## D[i,j] = if match available max(D[i-1,j]...)+1 else max(D[i-1,j]...)

def max_matches_mini(d,letter,strr,index_i,index_j):
	for i in range(len(strr)):
		if letter==strr[i]:
			return d+1,

def max_matches(D,Index_i,Index_j,str1,str2,i,j,flag):  ## i and j will be the actual indices + 1 and index_i will have index of last matched letter
	if flag==0:
		temp1 = 0
		temp2 = 0
		temp3 = 0
		temp1 = max_matches_mini(D[i-1,j],str1[i],str2[Index_j[i-1,j]+1:j],Index_i[i-1,j],Index_j[i-1,j])