import math
from datetime import datetime
from typing import Tuple, List, Dict

penalty, start, start2, last, ce, is_scored, is_time_format = input().split()

penalty, last, ce, is_scored, is_time_format = map(int, (penalty, last, ce, is_scored, is_time_format))
start = datetime.strptime(f"{start} {start2}", '%Y-%m-%d %H:%M:%S')

n = int(input())
problems: Dict[int, Tuple[int, int]] = {i[0]: (i[1], i[2]) for i in [tuple(map(int, input().split())) for _ in range(n)]} # type: ignore
problem_keys_sorted = list(problems.keys())
problem_keys_sorted.sort(key=lambda x: problems[x][0])

_ = input()
users = input().split()

s = int(input())
submits = [(int(i[0]), int(i[1]), i[2], int(i[3]), int(i[4]), int(i[5]), datetime.strptime(f"{i[6]} {i[7]}", '%Y-%m-%d %H:%M:%S')) for i in [input().split() for _ in range(s)]]
# submits.sort(key=lambda x: x[6])

is_good_submit_per_user_problem: Dict[str, Dict[int, bool]] = {i: {k: False for k in problems.keys()} for i in users}
is_correct_per_user_problem: Dict[str, Dict[int, bool]] = {i: {k: False for k in problems.keys()} for i in users}
max_score_per_user_problem: Dict[str, Dict[int, int]] = {i: {
    k: max([*(map(lambda x: problems[k][1] if is_scored and x[4] == 0 and x[5] == 0 else x[5], filter(lambda x: x[2] == i and x[1] == k and x[3] == 4, submits))), 0]) for k in problems.keys()
} for i in users}
penalty1_per_user_problem: Dict[str, Dict[int, int]] = {i: {k: 0 for k in problems.keys()} for i in users}
penalty2_per_user_problem: Dict[str, Dict[int, int]] = {i: {k: 0 for k in problems.keys()} for i in users}
last_submit_id_per_user: Dict[str, int] = {i: 0 for i in users}
last_correct_submit_id_per_user: Dict[str, int] = {i: 0 for i in users}
tries_per_user_problem: Dict[str, Dict[int, int]] = {i: {k: 0 for k in problems.keys()} for i in users}

for i in submits:
    if (ce and i[3] == 11) or i[3] == 13:
        continue

    user = i[2]

    if user not in users:
        continue

    last_submit_id_per_user[user] = i[0]
    if i[3] == 4 and (i[4] == 0 or (is_scored and i[5] > 0)):
        last_correct_submit_id_per_user[user] = i[0]
        is_correct_per_user_problem[user][i[1]] = True

    is_good_submit: bool
    if is_scored:
        is_good_submit = i[3] == 4 and (i[5] == max_score_per_user_problem[user][i[1]] or (i[4] == 0 and i[5] == 0))
    else:
        is_good_submit = i[3] == 4 and i[4] == 0

    if not is_good_submit and not is_good_submit_per_user_problem[user][i[1]]: # not yet solved
        penalty1_per_user_problem[user][i[1]] += penalty # penalty 1
        tries_per_user_problem[user][i[1]] += 1

    if is_good_submit:
        if not is_good_submit_per_user_problem[user][i[1]]: # firstly solved
            tries_per_user_problem[user][i[1]] += 1
            penalty2_per_user_problem[user][i[1]] += math.floor((i[6] - start).total_seconds() // 60)

        is_good_submit_per_user_problem[user][i[1]] = True

for i in users:
    for j in problems:
        if not is_good_submit_per_user_problem[i][j]:
            penalty1_per_user_problem[i][j] = 0

penalty1_per_user = {i: sum(penalty1_per_user_problem[i].values()) for i in users}
penalty2_per_user = {i: max(penalty2_per_user_problem[i].values()) if last else sum(penalty2_per_user_problem[i].values()) for i in users}
penalty_per_user = {i: penalty1_per_user[i] + penalty2_per_user[i] for i in users}
scores: Dict[str, int]

if is_scored:
    scores = {i: sum(max_score_per_user_problem[i].values()) for i in users}
else:
    scores = {i: sum(map(lambda x: 1, filter(lambda x: x, is_good_submit_per_user_problem[i].values()))) for i in users}

users.sort() # by id (5)
users.sort(key=lambda x: last_submit_id_per_user[x]) # by last submit (4)
users.sort(key=lambda x: last_correct_submit_id_per_user[x]) # by last good submit (3)
users.sort(key=lambda x: penalty_per_user[x]) # by penalty (2)
users.sort(key=lambda x: scores[x], reverse=True) # by score (1)


rank = 1
rank_score = scores[users[0]]
rank_penalty = penalty_per_user[users[0]]
rank_user = 0

for (idx, user) in enumerate(users):
    if rank_score == scores[user] and rank_penalty == penalty_per_user[user]:
        rank_user += 1
    else:
        rank += rank_user
        rank_user, rank_score, rank_penalty = 1, scores[user], penalty_per_user[user]

    l = [str(rank), user]

    for i in problem_keys_sorted:
        if is_correct_per_user_problem[user][i]:
            if is_scored:
                max_score = max_score_per_user_problem[user][i]
                p = penalty2_per_user_problem[user][i] if last else penalty1_per_user_problem[user][i] + \
                                                                    penalty2_per_user_problem[user][i]
                minute = f'{p // 60}:{str(p % 60).zfill(2)}'
                l.append(f'{"a" if max_score == problems[i][1] else "p"}/{max_score}/{tries_per_user_problem[user][i]}/{minute if is_time_format else p}')
            else:
                p = penalty2_per_user_problem[user][i] if last else penalty1_per_user_problem[user][i] + penalty2_per_user_problem[user][i]
                minute = f'{p // 60}:{str(p % 60).zfill(2)}'
                l.append(f'a/{tries_per_user_problem[user][i]}/{minute if is_time_format else p}')
        elif tries_per_user_problem[user][i] > 0:
            l.append(f'w/{tries_per_user_problem[user][i]}/--')
        else:
            l.append('0/--')

    minute = f"{(penalty_per_user[user])//60}:{str((penalty_per_user[user])%60).zfill(2)}"
    l.append(f'{scores[user]}/{minute if is_time_format else penalty_per_user[user]}')

    print(','.join(l))