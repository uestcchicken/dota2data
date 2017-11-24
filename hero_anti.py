import numpy as np
import math
import dota2api
import sys

hero_num = 120
api = dota2api.Initialise('85EAAACBEB46A84273D29DCF1A777246')

def get_hero_name_list():
    hero_dict = api.get_heroes()
    heroes = hero_dict['heroes']
    heroes.sort(key = lambda k: (k.get('id'), 0))
    name_list = ['unused'] * (hero_num + 1)
    for i in range(len(heroes)):
        name_list[heroes[i]['id']] = heroes[i]['localized_name']
    return name_list

self_rate = np.load('hero_self_rates.npy')
mutual_rate = np.load('hero_mutual_rates.npy')
anti = np.zeros((hero_num + 1, hero_num + 1))

for i in range(1, hero_num + 1):
    for j in range(1, hero_num + 1):
        if i == j or np.isnan(self_rate[i]) or np.isnan(self_rate[j]):
            anti[i][j] = 0
        else:
            expected_rate = self_rate[i] / (self_rate[i] + self_rate[j])
            actual_rate = mutual_rate[i][j]
            
            #anti[i][j] = - math.log(self_rate[i]) / math.log(actual_rate) / math.log(self_rate[j])
            anti[i][j] = - math.log(0.4) / math.log(0.5) / math.log(0.4)

name_list = get_hero_name_list()
for i in range(1, 6):
    if len(sys.argv) == 1:
        top = anti.argmax()
        x = (int)(top / 121)
        y = top % 121
        print('top ', i, ': ')
        print(name_list[x], 'rate: ', self_rate[x])
        print(name_list[y], 'rate: ', self_rate[y])
        #print('expected rate: ', self_rate[x] / (self_rate[x] + self_rate[y]))
        print('actual rate: ', mutual_rate[x][y])
        print('score: ', anti[x][y])
        print('********************************')
        anti[x][y] = 0
    else:
        hero_id = int(sys.argv[1])
        hero_anti = anti[hero_id]
        top = hero_anti.argmax()
        x = hero_id
        y = top
        print('top ', i, ': ')
        print(name_list[x], 'rate: ', self_rate[x])
        print(name_list[y], 'rate: ', self_rate[y])
        #print('expected rate: ', self_rate[x] / (self_rate[x] + self_rate[y]))
        print('actual rate: ', mutual_rate[x][y])
        print('score: ', anti[x][y])
        print('********************************')
        anti[x][y] = 0
        
        
        
        
        
        
        
        
        
        
        
        
        