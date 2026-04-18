import math

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
arr_ = ''.join(map(lambda x: ''.join(x), arr))
actions = input()

monsters = {}
is_boss_dead = False
killer = ''

for _ in range(arr_.count('&') + 1):
    y, x, name, w, a, h, e = input().split()
    monsters[(int(y) - 1, int(x) - 1)] = tuple(map(int, (w, a, h, h, e))) + (name,) # atk, vit, hp, max_hp, exp

chests = {}

for _ in range(arr_.count('B')):
    y, x, t, s = input().split()
    chests[(int(y)-1, int(x)-1)] = (t, int(s) if t == 'W' or t == 'A' else s)

pos = (0, 0)
turns = 0

hp, max_hp, atk, vit = 20, 20, 2, 2
weapon_atk, armor_vit = 0, 0
level = 1
exp = 0
equipments = set()

for y in range(n):
    if '@' in arr[y]:
        pos = (y, arr[y].index('@'))

initial_pos = pos

arr[pos[0]][pos[1]] = '.'

def maybe_death() -> bool:
    global pos, hp

    if 'RE' in equipments:
        pos = initial_pos
        hp = max_hp

        if arr[pos[0]][pos[1]] in ('&', 'M'):
            monsters[pos][2] = monsters[pos][3]

        equipments.remove('RE')
        
        return False

    return True

def heal(amount: int):
    global hp
    hp = min(hp + amount, max_hp)

def maybe_lvup():
    global exp, level, max_hp, hp, atk, vit

    if exp >= 5*level:
        exp = 0
        level += 1

        max_hp += 5
        hp = max_hp
        atk += 2
        vit += 2

for action in actions:
    turns += 1

    next_pos = (
        pos[0] + (1 if action == 'D' else -1 if action == 'U' else 0),
        pos[1] + (1 if action == 'R' else -1 if action == 'L' else 0),
    )

    if (not 0 <= next_pos[0] < n) or (not 0 <= next_pos[1] < m) or arr[next_pos[0]][next_pos[1]] == '#': next_pos = pos

    pos = next_pos

    match arr[pos[0]][pos[1]]:
        case '^':
            hp -= (5 if 'DX' not in equipments else 1)

            if hp <= 0:
                if maybe_death():
                    killer = 'SPIKE TRAP'
                    break
                else: continue
        case 'B':
            item = chests[pos]
            if item[0] == 'W':
                atk -= weapon_atk
                atk += item[1]
                weapon_atk = item[1]
            elif item[0] == 'A':
                vit -= armor_vit
                vit += item[1]
                armor_vit = item[1]
            else:
                if len(equipments) < 4:
                    equipments.add(item[1])
            arr[pos[0]][pos[1]] = '.'
        case '&' | 'M':
            enemy = monsters[pos]
            enemy_hp = enemy[2]
            is_first = True
            is_boss = arr[pos[0]][pos[1]] == 'M'

            if is_boss and 'HU' in equipments:
                hp = max_hp

            while True:
                damage = max(1, (atk * (1 if 'CO' not in equipments or not is_first else 2 if 'DX' not in equipments else 3))-enemy[1])
                enemy_hp -= damage

                if enemy_hp <= 0: break

                damage = 0 if is_boss and is_first and 'HU' in equipments else max(1, enemy[0]-vit)
                hp -= damage

                if hp <= 0: break

                is_first = False

            if enemy_hp <= 0:
                arr[pos[0]][pos[1]] = '.'
                exp += math.floor(enemy[4] * (1 if 'EX' not in equipments else 1.2))
                maybe_lvup()

                if 'HR' in equipments:
                    heal(3)

                if is_boss:
                    is_boss_dead = True
                    break
            elif maybe_death():
                killer = enemy[5]
                break
            else:
                continue

if hp > 0:
    arr[pos[0]][pos[1]] = '@'

print('\n'.join(map(lambda x: ''.join(x), arr)))
print(f"Passed Turns : {turns}")
print(f'LV : {level}')
print(f'HP : {max(hp, 0)}/{max_hp}')
print(f'ATT : {atk-weapon_atk}+{weapon_atk}')
print(f'DEF : {vit-armor_vit}+{armor_vit}')
print(f'EXP : {exp}/{5*level}')
print('YOU WIN!' if is_boss_dead else f'YOU HAVE BEEN KILLED BY {killer}..' if killer != '' else 'Press any key to continue.')