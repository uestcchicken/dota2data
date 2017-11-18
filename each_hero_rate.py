'''
calculate win rate for each hero alone

read from matches.dat
save to hero_rates.npy
'''

import numpy as np 

hero_num = 120

file = open("matches.dat")

arr_wins = np.zeros(hero_num)
arr_loses = np.zeros(hero_num)
arr_rate = np.zeros(hero_num)

counter = 0

while 1:
	line = file.readline()
	if not line:
		break

	counter += 1
	
	data = line.split()
	
	for i in range(0, 5):
		arr_wins[int(data[i]) - 1] += 1
	for i in range(5, 10):
		arr_loses[int(data[i]) - 1] += 1

print(arr_wins)
print(arr_loses)

arr_rate = arr_wins / (arr_wins + arr_loses)
print(arr_rate)

np.save('hero_rates', arr_rate)