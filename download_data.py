'''
download match data 

read from latest.dat
save to latest.dat
save to matches.dat
'''

import dota2api
api = dota2api.Initialise('85EAAACBEB46A84273D29DCF1A777246')

counter = 0

while 1:
	f_latest = open('latest.dat', 'r')
	
	latest = int(f_latest.readline())
	latest += 1
	f_latest.close()


	matches_got = api.get_match_history_by_seq_num(matches_requested = 20, start_at_match_seq_num = latest)

	f_data = open('matches.dat', 'a')
	matches = matches_got['matches']

	for m in matches:
		id = m['match_id']
		heroes = []
		win = m['radiant_win']
		players = m['players']

		if len(players) != 10:
			continue
		for p in players:
			hero_id = p['hero_id']
			heroes.append(hero_id)

		radiant_team = heroes[0:5]
		dire_team = heroes[5:10]
		radiant_team.sort()
		dire_team.sort()
		if radiant_team[0] == 0:
			continue
		if dire_team[0] == 0:
			continue

		if win: 
			win_team = radiant_team
			lose_team = dire_team
		else:
			win_team = dire_team
			lose_team = radiant_team
		latest = m['match_seq_num']
		counter += 1
		print(counter, id, win, win_team, lose_team, latest)
		for h in win_team:
			f_data.write(str(h) + ' ')
		for h in lose_team:
			f_data.write(str(h) + ' ')
		f_data.write(str(latest))
		f_data.write('\n')

	f_update = open('latest.dat', 'w')
	f_update.writelines(str(latest))
	f_update.close()
	f_data.close()


