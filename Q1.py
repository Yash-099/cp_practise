import numpy as np

##### D(i) = min(D(i-1)+1,D(i-3)+1,D(i-4)+1)


def min_coins(D_1,D_3,D_4):
  if D_1 == min(D_1,min(D_4,D_3)):
   return D_1 + 1, '1'
  elif D_3 == min(D_1,min(D_4,D_3)):
   return D_3+1,'3'
  else:
   return D_4+1,'4'



if __name__ == '__main__':
  amount = 10000
  listt_orig = []
  listt_1 = []
  listt_2 = []
  listt_3 = []
  listt_4 = []

  D = np.zeros(amount+1)
  D[1] = 1
  
  D[2] = 2
  
  D[3] = 1
  
  D[4] = 1

  listt_1 = [4]
  listt_2 = [3]
  listt_3 = [1,1]
  listt_4 = [1]

  holder_1 = []
  holder_2 = []
  holder_3 = []
  holder_4 = []
  
  for i in range(5,amount+1):
    D[i],temp = min_coins(D[i-1],D[i-3],D[i-4])
    if temp=='1':
      listt_orig = listt_1+[1]
    elif temp=='3':
      listt_orig = listt_3+[3]
    elif temp=='4':
      listt_orig = listt_4+[4]

    listt_4 = listt_3
    listt_3 = listt_2
    listt_2 = listt_1
    listt_1 = listt_orig
    
    # print(D)
    # listt.append(listt[len(listt)-int(temp)].append(int(i)))


  print(int(D[amount]))
  print(listt_orig)