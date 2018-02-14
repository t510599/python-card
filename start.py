import random
import game
import card

# choose player
character = dict()
name=["安","圭月","梅","小兔","銀","正作","W","桑德","海爾","雪村"]
for i in range(len(name)):
	character[str(i+1)] = name[i] 

print("1.安，特殊能力:上帝視角，每回合一次，可以無視敵方玩家的指定")
print("2.圭月，特殊能力:空間拉鍊，可使用「傳送」、「狹縫」或「暴走」三張特殊手牌各一張")
print("3.梅，特殊能力:鮮血之梅，自己的回合開始時，使敵方玩家使其受到一點傷害，再回復自己一點生命值")
print("4.小兔，特殊能力:科學無用論，對敵方玩家造成的傷害加二")
print("5.銀，特殊能力:空氣制約，自己的回合開始時，使敵方玩家選擇棄掉兩張手牌或受到一點傷害")
print("6.正作，特殊能力:能量轉移，被敵方玩家指定並受到傷害時，可以棄掉三張手牌，無視敵方玩家的攻擊並給予那個玩家兩倍傷害")
print("7.W，特殊能力:歡迎來到輸家之國，當自己的生命值為三時，受到的傷害減二，自己的回合結束時給予敵方玩家兩點傷害")
print("8.桑德，特殊能力:安魂曲，每當自己丟棄手牌時，根據丟棄的張數敵方玩家等量的傷害或回復自己等量的生命值")
print("9.海爾，特殊能力:地獄之炎，自己的回合開始時，可以丟棄一張手牌，敵方玩家兩點傷害")
print("10.雪村，特殊能力:峰頂之冰，自己的回合開始時，可以丟棄三張手牌，使敵方玩家於下個回合無法發動能力")
print("喔對了 角色技能開發中 所以還不能用")

choice = input("玩家一，選擇你的角色 ")
while choice not in map(lambda x : str(x+1),list(range(len(name)))):
    choice = input("玩家一，選擇你的角色 ")
p1_name = character[choice]
print("玩家一",p1_name)
del choice # prevent reading the old data
print("") # change line
choice = input("玩家二，選擇你的角色 ")
while choice not in map(lambda x : str(x+1),list(range(len(name)))):
    choice = input("玩家一，選擇你的角色 ")
p2_name = character[choice]
print("玩家二",p2_name)
del choice # release resource

# create player object
p1 = game.Player(p1_name,card.default_deck)
p2 = game.Player(p2_name,card.default_deck)

# game start
first = random.choice([p1,p2])
first.playing = True # so the first one will be random
print(first.name,"先攻")
print("") # change line
for _ in range(3): # 初始手牌*3
    game.draw(p1)
    game.draw(p2)

while p1.life > 0 and p2.life > 0:
    game.turn(p1,p2)

if p1.life <= 0:
    print("{} 獲勝".format(p2.name))
elif p2.life <= 0:
    print("{} 獲勝".format(p1.name))