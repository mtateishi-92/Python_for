import random

print('じゃんけんを始めます。')
player_input = input('数字を入力してください（0：グー、1：チョキ、3：パー）：')
lists = {0:'グー', 1:'チョキ', 2:'パー'}

int(player_input)

player = lists[player_input]
com = random.choice(lists)
print(player)
#print(com)
for com_list in lists:
    if 'グー' == 'グー':
        print('COMは'+ com +'をだしました。')
    if 'チョキ' == 'チョキ':
        print('COMは'+ com +'をだしました。')
    if 'パー' == 'パー':
        print('COMは'+ com +'をだしました。')
