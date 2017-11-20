import dota2api
api = dota2api.Initialise('85EAAACBEB46A84273D29DCF1A777246')

matches_h = api.get_match_history(matches_requested = 10)
#matches_h = api.get_match_history_by_seq_num(matches_requested = 10, start_at_match_seq_num = 3100000000)
matches = matches_h['matches']

for m in matches:
    m_id = m['match_id']
    seq = m['match_seq_num']
    print(m_id, seq)