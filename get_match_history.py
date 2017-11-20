import dota2api
import sys
#初始化api
api = dota2api.Initialise('85EAAACBEB46A84273D29DCF1A777246')

#英雄ID中的最大值
MAX_NUM = 120
def get_hero_name_list():
    hero_dict = api.get_heroes()
    #英雄ID和名字列表
    heroes = hero_dict['heroes']
    #根据ID排序
    heroes.sort(key = lambda k: (k.get('id'), 0))
    #有部分ID未被使用，如24
    name_list = ['unused'] * (MAX_NUM + 1)
    for i in range(len(heroes)):
        name_list[heroes[i]['id']] = heroes[i]['localized_name']
    return name_list

def win_or_lose(m_id, player_slot):
    #确定玩家位置，True为天辉False为夜魇
    if player_slot < 5:
        side = True
    else:
        side = False
    detail = api.get_match_details(m_id)
    #获取比赛胜负
    win_side = detail['radiant_win']
    #比较判断
    if side == win_side:
        return 'win '
    else:
        return 'lose'
    
#我的dota2用户ID
my_id = sys.argv[1]
matches = sys.argv[2]
#调用get_match_history函数
match_history = api.get_match_history(account_id = my_id, matches_requested = matches)
#解析获得的match_history字典对象，取其中的matches键
matches = match_history['matches']

name_list = get_hero_name_list()

#逐个解析每场比赛
for m in matches:
    #获取比赛ID
    m_id = m['match_id']
    #获取所有玩家
    players = m['players']
    #逐个解析每个玩家
    for p in players:
        #寻找自己
        if p['account_id'] == int(my_id):
            #获取所用英雄ID
            h_id = p['hero_id']
            h_name = name_list[h_id]
            result = win_or_lose(m_id, p['player_slot'])
            break
    print('match id: ', m_id, 'result: ', result, 'hero: ', h_name)

