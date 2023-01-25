import random
import colorama
from colorama import Fore,Style
"""
ver1.0
完成:
    基本功能
未來:
    攻擊卡
    特殊連擊
    對話
"""
global deck
deck = []
for i in range(4):
    #deck.append("Explode kitten")
    deck.append("Attack")
    deck.append("Favor")
    deck.append("Shuffle")
    deck.append("Cat card")
    deck.append("Skip")
for i in range(5):
    deck.append("Nope")
    deck.append("See the future")
random.shuffle(deck)
#for i in range(6):
    #deck.append("Defuse")
"""
抽卡函式 參數=張
全域 玩家卡牌庫
運行num次
回傳 玩家卡牌庫
"""

def draw(num):   
    l= []
    for i in range(num):
        l.append(deck[0])
        del deck[0]
    if len(l)>1:
        return l
    else:
        l2="".join(l)
    return l2
global player_deck,player_num,turn
player_deck = []
while True:
    try:
        player_num =int(input("人數"))
        if not 1<player_num<6:
            raise
        break
    except:
        print("請輸入正確人數(2~5)")
        continue
for i in range(player_num):
    player_deck.append(draw(7))
for num in range(0,player_num):
    player_deck[num].append("Defuse")
for i in range(player_num-1):
    deck.append("Explode kitten")
for i in range(6-player_num):
    deck.append("Defuse")#炸彈貓 拆彈卡放回去
for i in range(5):
    random.shuffle(deck)#洗5次牌
"""
看手牌函式
show(玩家索引12345):
"""
    
def color_print(l,e):
    if type(l)!=list:
        l=[l]
    t=1
    for i in l:
        if i == "Attack":
            print(f"{t})",Fore.RED + i + Style.RESET_ALL , end=e)
        elif i == "Favor":
            print(f"{t})",Fore.LIGHTYELLOW_EX + i + Style.RESET_ALL , end=e)
        elif i == "Shuffle":
            print(f"{t})",Fore.LIGHTBLUE_EX + i + Style.RESET_ALL , end=e)
        elif l == "Cat card":
            print(f"{t})",Fore.YELLOW + i +Style.RESET_ALL , end=e)
        elif i == "Skip":
            print(f"{t})",Fore.LIGHTRED_EX+ i +Style.RESET_ALL , end=e)
        elif i == "Nope":
            print(f"{t})",Fore.LIGHTBLACK_EX + i + Style.RESET_ALL , end=e)
        elif i == "See the future":
            print(f"{t})",Fore.LIGHTMAGENTA_EX + i +Style.RESET_ALL , end=e)
        elif i == "Exploding cat":
            print(f"{t})",Fore.LIGHTRED_EX + i + Style.RESET_ALL , end=e)
        elif i == "Defuse":
            print(f"{t})",Fore.LIGHTGREEN_EX + i + Style.RESET_ALL , end=e)
        else:
            print(f"{t})",i,end=e)
        t+=1
    print()


def show(n): #要看的人
    print(Fore.MAGENTA + f"Player{n+1}:" + Style.RESET_ALL)
    print("--------------")
    color_print(player_deck[n],"\n")

for num in range(0,len(player_deck)):#開局看手牌(全部人)
    show(num)
print("///////////////////////////////")
#牌已分發完畢 開始遊戲
"""
deck 牌庫
fold_area 棄牌區#
player_deck 玩家牌庫(只儲存玩家的卡牌)
player_num 總人數
turn 回合玩家索引#
card_num 卡牌索引
text 指令
Accept 流程正確可使用
"""
fold_area = []
turn=0
turn_list =[]
for i in range(player_num):
    turn_list.append(i)
#Accept = True
#gaming
show(turn)

def run(c,t):
    if c == "Favor":
        while True:
            try:
                favor_player = int(input("選擇一個玩家:P"))
                if favor_player == t:
                    raise
                break
            except:
                print("輸入錯誤玩家")
                continue
        show(favor_player-1)
        while True:
            try:
                favor_card = int(input("Choose a card you want to give"))
                if favor_card >= len(player_deck[favor_player-1]):
                    raise
                break
            except:
                print("輸入錯誤索引")
                continue

        favor_card_index = player_deck[favor_player-1].index(player_deck[favor_player-1][favor_card])
        player_deck[t].append(player_deck[favor_player-1][favor_card_index])
        print(f"已給予-{player_deck[favor_player-1][favor_card_index]}")
        del player_deck[favor_player-1][favor_card_index]

    elif c== "Shuffle":
        print("\n洗牌中")
        random.shuffle(deck)
        print(f"還是Player{turn+1}的回合!")
    elif c == "See the future":
        print("\n接下來的三張為")
        color_print(deck[0:3],"\n")
        print(f"還是Player{turn+1}的回合!")
    elif c == "Defuse":
        print("拆除炸彈!")
#attack先不寫出來

def gaming(turn):
    while True:
        try:
            card_num = input(f"Player{turn+1}請出牌:")#12345
            if card_num == "抽牌":
                break
            elif card_num == "我要看手牌":
                show(turn)
                raise
            card_num = int(card_num)
            card = player_deck[turn][card_num-1]
            if 0<card_num<len(player_deck[turn]) and card != "Nope":#卡牌索引正確
                check_nope_list = [i for i in range(0,player_num)]
                check_nope_list.remove(turn)
                for i in check_nope_list:
                    if "Nope" in player_deck[i] or card!="Defuse" or card!="Exploding cat":#除了本回合玩家以外的人只要有nope 斷迴圈開始詢問
                        while True:
                            try:
                                ask_want_to_draw = eval(input("我們之中有禁止卡(12345)\n若不想出牌請輸入任何字元"))
                                if ask_want_to_draw-1 in [i for i in range(0,player_num+1)] and ask_want_to_draw-1 != turn:
                                    Skip_index =player_deck[ask_want_to_draw-1].index("Nope")
                                    print("休想!!!")
                                    del player_deck[ask_want_to_draw-1][Skip_index]
                                    break
                                elif ask_want_to_draw-1 == turn:
                                    print("\n輸入錯誤")
                                    continue
                                else:
                                    raise
                            except:
                                print("\n沒人要禁止 執行")
                                if card == "Skip":
                                    break
                                else:
                                    run(card,turn)
                                    break
                    else:
                        run(card,turn)
                        break
            else:
                print("索引錯誤")
                raise TypeError("輸入的數字索引值錯誤")                 
        except:
            print(f"還是Player{turn+1}的回合!")
            continue
    
       
while player_num !=1:
    #完整一回合
    gaming(turn)
    final=draw(1)
    print(f"Player{turn+1}抽到的是",end="")
    color_print(final,"")
    if final == "Exploding cat":
        for i in player_deck[turn]:
            if i == "Defuse":
                print("拆除炸彈成功!!!")
                random.shuffle(deck)
                break
            else:
                print(f"你輸了!Player{turn+1}")
                player_num-=1
                turn_list.remove(turn)
                break
    else:
        player_deck[turn].append(final)
    while player_num!=1:
        turn+=1
        if turn > turn_list[len(turn_list)-1]:
            turn=turn_list[0]
            break
        elif turn not in turn_list:
            turn+=1
            break
        elif turn in turn_list:
            break

turn_list[0] = turn_list[0]+1
print("贏家是{}".format(turn_list))