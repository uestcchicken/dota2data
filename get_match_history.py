import dota2api
#初始化api
api = dota2api.Initialise()

#我的dota2用户id
my_id = 192609391
#调用get_match_history函数
match_history = api.get_match_history(account_id = my_id, matches_requested = 5)

#解析获得的match_history字典对象，取其中的matches键
matches = match_history['matches']
#逐个解析每场比赛
for m in matches:
    #获取比赛id
    m_id = m['match_id']
    #获取所有玩家
    players = m['players']
    #逐个解析每个玩家
    for p in players:
        #寻找自己
        if p['account_id'] == my_id:
            #获取所用英雄id
            h_id = p['hero_id']
    print("match id:", m_id, "hero:", h_id)
