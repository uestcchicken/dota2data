'''
calculate win rate for each hero alone

read from matches.dat
save to hero_self_rates.npy
'''

import numpy as np 

hero_num = 120

f = open("matches.dat")

arr_wins = np.zeros(hero_num + 1)
arr_loses = np.zeros(hero_num + 1)
arr_rate = np.zeros(hero_num + 1)

counter = 0

while 1:
	line = f.readline()
	if not line:
		break
	counter += 1
	
	data = line.split()
	for i in range(0, 5):
		arr_wins[int(data[i])] += 1
	for i in range(5, 10):
		arr_loses[int(data[i])] += 1
f.close()
print('match num: ', counter)
print(arr_wins)
print(arr_loses)

arr_rate = arr_wins / (arr_wins + arr_loses)
print(arr_rate)

np.save('hero_self_rates', arr_rate)