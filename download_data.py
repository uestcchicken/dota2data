'''
download match data 

read from latest.dat
save to latest.dat
save to matches.dat
'''

import dota2api
import time
import json
api = dota2api.Initialise('85EAAACBEB46A84273D29DCF1A777246')

counter = 0

while 1:
	#读取已下载的最新比赛的sequence_id
	f_latest = open('latest.dat', 'r')
	latest = int(f_latest.readline())
	latest += 1
	f_latest.close()
	#调用API获取比赛信息
	while(1):
		try:
			data_got = api.get_match_history_by_seq_num(matches_requested = 20, start_at_match_seq_num = latest)
		except json.decoder.JSONDecodeError:
			print('error, wait 10 seconds.************************************************************')
			time.sleep(10)
			continue
		else:
			break

	matches = data_got['matches']
	#写入文件
	f_data = open('matches.dat', 'a')
	#对获取的每场比赛
	for m in matches:
		#比赛ID
		id = m['match_id']
		heroes = []
		#获胜方
		win = m['radiant_win']
		#所有玩家
		players = m['players']
		#排除人数不为10的，如solo
		if len(players) != 10:
			print('player num error: ', len(players))
			continue
		#获取所有上场英雄
		for p in players:
			hero_id = p['hero_id']
			heroes.append(hero_id)
		#天辉英雄
		radiant_team = heroes[0:5]
		#夜魇英雄
		dire_team = heroes[5:10]
		#按ID排序
		radiant_team.sort()
		dire_team.sort()
		#排除英雄ID错误
		if radiant_team[0] == 0:
			print('player hero error: 0')
			continue
		if dire_team[0] == 0:
			print('player hero error: 0')
			continue
		#按获胜方和战败方存储英雄ID
		if win: 
			win_team = radiant_team
			lose_team = dire_team
		else:
			win_team = dire_team
			lose_team = radiant_team
		#当前比赛的sequence_id
		latest = m['match_seq_num']
		counter += 1
		print(counter, id, win, win_team, lose_team, latest)
		#写入文件
		for h in win_team:
			f_data.write(str(h) + ' ')
		for h in lose_team:
			f_data.write(str(h) + ' ')
		f_data.write(str(latest))
		f_data.write('\n')
	#更新latest.dat
	f_update = open('latest.dat', 'w')
	f_update.writelines(str(latest))
	f_update.close()
	f_data.close()


