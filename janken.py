import random

print('じゃんけんを始めます。')
player_input = input('数字を入力してください（0：グー、1：チョキ、2：パー）：')
lists = ['グー', 'チョキ', 'パー']

player = lists[int(player_input)]
com = random.choice(lists)

print('あなたは' + player + 'をだしました。')
print('COMは'+ com +'をだしました。')

if player == 'グー' and com == 'グー':
    print('引き分けです。')
if player == 'チョキ' and com == 'チョキ':
    print('引き分けです。')
if player == 'パー' and com == 'パー':
    print('引き分けです。')

if player == 'グー' and com == 'チョキ':
    print('あなたの勝ちです。')
if player == 'チョキ' and com == 'パー':
    print('あなたの勝ちです。')
if player == 'パー' and com == 'グー':
    print('あなたの勝ちです。')

if player == 'グー' and com == 'パー':
    print('あなたの負けです。')
if player == 'チョキ' and com == 'グー':
    print('あなたの負けです。')
if player == 'パー' and com == 'チョキ':
    print('あなたの負けです。')