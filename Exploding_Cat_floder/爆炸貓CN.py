import random
import colorama
from colorama import Fore, Style
import time
import os

class IndexError(Exception):
    pass
class SkipException(Exception):
    pass
class CheckNopeException(Exception):
    pass

def cls():
    os.system("cls")

def talk(n):
    for i in n:
        print(i,end="")
        time.sleep(0.1)
    print()

global used_list,deck
deck = []
for i in range(4):
    #deck.append("Explode kitten")
    deck.append("攻擊卡")
    deck.append("恩惠卡")
    deck.append("洗牌卡")
    deck.append("跳過卡")
for i in range(5):
    deck.append("休想卡")
    deck.append("預知未來")
for i in range(4):
    deck.append("塔可貓")
    deck.append("毛茸茸馬鈴薯貓")
    deck.append("瓜貓")
    deck.append("鬍子貓")
    deck.append("嘔吐彩虹貓")
random.shuffle(deck)

"""
抽卡函式 參數=張
全域 玩家卡牌庫
運行num次
回傳 玩家卡牌庫
"""
def plot():
    cls()
    def restart():
        input("-你有想過為什麼鐵達尼號會沉沒嗎?\n")
        input("-不...不是老掉牙的黃色笑話\n")
        input("-其實都是因為貓咪在船上搗亂才沉沒的!!!\n")
        input("-不相信?玩過這款滿滿都是貓咪的爆炸貓你就會相信了~~\n")
        input("講解規則?\n")
        input("-本遊戲支援2~5人\n")
        input(" 這邊還是做個簡單的教學 遊戲規則超級超級簡單!\n")
        input("-遊戲開始前:")
        print(" 1.挑出所有的爆炸貓卡和拆除卡 然後發給每個玩家七張牌")
        print(" 2.發給每位玩家一張拆除牌")
        print(" 3.將人數-1數量的爆炸貓卡和`剩下的拆除卡洗進牌堆 沒用到的爆炸貓卡放回盒子")
        print(" 4.準備開始刺激的爆炸貓!\n")
    def start_rule():
        input("-遊戲開始:\n")
        input(" 當輪到你的回合時 你只有兩個選擇\n")
        input(" 1.跳過:不出任何牌 從牌庫抽一張卡牌後 結束回合\n")
        input(" 2.出牌:出任意數量的功能牌 結算結果後 從牌庫抽一張卡牌 結束回合\n")
        input("-如果抽到爆炸貓呢?\n")
        input(" BOOOOOOOOM\n")
        input(" 你被炸死了 淘汰!!!\n")
        input(" 有人被炸死的時候 他要丟掉所有的手牌 然後也丟掉讓他爆炸的那張爆炸貓卡\n")
        input(" 遊戲會一直持續到剩下最後一位倖存者。\n")
        input("-恭喜你! 你活下來了!!!\n")
    def special_card_rule():
        input("-若要贏得勝利 你需要活用功能卡的效果!!!\n")
        input("-預見未來卡:\n 可以偷看接下來三張牌 知道有沒有爆炸的危險\n")
        input("-跳過卡:\n 可以不用抽牌就結束這個回合 在知道下一張可能會爆炸的時候可以保住一命\n")
        input("-洗混卡:\n 將牌堆重洗 可以製造混亂\n")
        input("-攻擊卡:\n 打出這張牌可以不用抽牌就結束回合 而且你的對手接下來要進行兩個回合[抽兩張牌]\n")
        input("-恩惠卡:\n 可以強迫一個人給你一張手牌[被指定的人決定給哪一張] 如果對方只剩拆除卡就一定能拿到\n")
        input("-拆除卡:\n 每個人一開始都會拿到一張 可以防止爆炸\n 把剛剛抽到的爆炸貓卡偷偷塞到牌庫裡的隨便一個位置 也可以直接塞到下一張來陷害人\n")
        input("-休想卡:\n 可以隨時打出來 讓對手的行動無效 也可以無效別人的無效\n")
        input("-貓咪卡:\n 有五種 只有一張的話沒什麼用 但是湊起來的話會有強大的功能...\n")
        input("-補充規則:\n")
        input(" 1.被攻擊卡攻擊時 可以丟出攻擊卡來跳過自己的回合 並讓下一回合的玩家吃到效果")
        input(" 2.承1 可以丟出跳過卡 但只能跳過一回合 若要完全解除 需要2張")
        input(" 3.禁止卡可以阻止除了炸彈貓 拆除卡 以外的卡牌(包括特殊聯集)\n")
    def special_combo_rule():
        input("-特殊連擊:\n")
        input(" 成雙成對:\n 打出兩張相同的卡(Ex.一對休想卡)你可以從其他玩家手上拿一張卡加入手牌\n")
        input(" 三條:\n 和成雙成對的效果差不多 但是你可以直接對玩家說出你想要的卡\n 如果對方有 就要立刻拿給你 反之 你什麼也拿不到...\n")
        input(" 5張卡牌面不同:\n 如果你在自己陷入困境的時候有5張標題不同的卡 把這幾張卡放在棄牌區 並且從棄牌區拿一張你喜歡的卡\n")

    restart()
    start_rule()
    special_card_rule()
    special_combo_rule()
    while True:
        ans=input("\"喵喵??\"(準備好了嗎?)\n[任意]開始遊戲 / [R]重看規則 / [1]遊戲基礎規則 / [2]功能卡規則 / [3]特殊連擊\n")
        if ans=="R" or ans=="r":
            plot()
        elif ans=="1":
            cls()
            start_rule()
        elif ans=="2":
            cls()
            special_card_rule()
        elif ans=="3":
            cls()
            special_combo_rule()
        else:
            break
cls()
print("-第一次玩???")
start_plot=input("[任意]開始遊戲 [N]我想知道怎麼玩")
if start_plot=="N" or start_plot=="n":
    print()
    plot()
else:
    print()
    pass

def message(kind,t):
    t=t+1
    if kind=="爆炸貓" or kind=="Explode kitten":
        talk("\n\"嘶......\"")
        input()
        input("(爆炸聲\n")
        a=input("\"跟這個世界說再見 順便說該死的貓咪\"")

    elif kind=="拆除卡" or kind=="Defuse":
        talk("\n\"嘶......\"")
        input()
        input("(喀擦!\n")

    elif kind=="Put Explode kitten":
        input("\n\"我看到你露出了奸笑 你是不是把貓咪放在第一張?\"")

    elif kind=="預知未來" or kind=="See the future":
        input("\n\"其實你只想知道明天的樂透號碼\"")

    elif kind=="攻擊卡" or kind=="Attack":
        input(f"\n\"這張被打出來的時機 通常是對方已經知道未來有爆炸貓了 所以盡快反擊吧!!\"")

    elif kind=="恩惠卡" or kind=="Favor":
        l=["\n\"這才不是偷 這叫好人有好報\"","\n\"感謝你的牌 雖然我知道你很不情願給我\""]
        input(random.choice(l))
    
    elif kind=="跳過卡" or kind=="Skip":
        input("\n\"看到炸彈貓就溜之大吉了齁~\"")

    elif kind=="洗牌卡" or kind=="Shuffle":
        l=["\n\"請記得喊停呀！洗牌洗到手抽筋\"","\n\"人生最悲慘的時刻 洗完牌還是爆炸貓\""]
        input(random.choice(l))
    else:
        pass

def draw(num):
    l = []
    for i in range(num):
        l.append(deck[0])
        del deck[0]
    if len(l) > 1:
        return l
    else:
        l2 = "".join(l)
    return l2

player_deck = []
while True:
    try:
        player_num = int(input("現場有多少玩家呢:"))
        if not 1 < player_num < 6:
            raise
        break
    except:
        print("請輸入正確人數(2~4)")
        continue

for i in range(player_num):
    player_deck.append(draw(7))
for num in range(0, player_num):
    player_deck[num].append("拆除卡")
for i in range(player_num - 1):
    deck.append("爆炸貓")
for i in range(6 - player_num):
    deck.append("拆除卡")  #炸彈貓 拆彈卡放回去

for i in range(5):
    random.shuffle(deck)  #洗5次牌
"""
看手牌函式
show(玩家索引12345):
"""

def color_print(l, e):
    if type(l) != list:
        if l == "攻擊卡":
            print(Fore.RED + l + Style.RESET_ALL, end=e)
        elif l == "恩惠卡":
            print(Fore.LIGHTYELLOW_EX + l + Style.RESET_ALL, end=e)
        elif l == "洗牌卡":
            print(Fore.LIGHTBLUE_EX + l + Style.RESET_ALL, end=e)
        elif l == "跳過卡":
            print(Fore.LIGHTCYAN_EX + l + Style.RESET_ALL, end=e)
        elif l == "休想卡":
            print(Fore.LIGHTBLACK_EX + l + Style.RESET_ALL, end=e)
        elif l == "預知未來":
            print(Fore.LIGHTMAGENTA_EX + l + Style.RESET_ALL, end=e)
        elif l == "爆炸貓":
            print(Fore.LIGHTRED_EX + l + Style.RESET_ALL, end=e)
        elif l == "拆除卡":
            print(Fore.LIGHTGREEN_EX + l + Style.RESET_ALL, end=e)
        elif l == "特殊連擊":
            print(Fore.LIGHTRED_EX + l + Style.RESET_ALL, end=e)
        else:
            print(l, end=e)
    else:
        t = 1
        for i in l:
            if i == "攻擊卡":
                print(f"{t})", Fore.RED + i + Style.RESET_ALL, end=e)
            elif i == "恩惠卡":
                print(f"{t})", Fore.LIGHTYELLOW_EX + i + Style.RESET_ALL, end=e)
            elif i == "洗牌卡":
                print(f"{t})", Fore.LIGHTBLUE_EX + i + Style.RESET_ALL, end=e)
            elif i == "跳過卡":
                print(f"{t})", Fore.LIGHTCYAN_EX + i + Style.RESET_ALL, end=e)
            elif i == "休想卡":
                print(f"{t})", Fore.LIGHTBLACK_EX + i + Style.RESET_ALL, end=e)
            elif i == "預知未來":
                print(f"{t})", Fore.LIGHTMAGENTA_EX + i + Style.RESET_ALL, end=e)
            elif i == "爆炸貓":
                print(f"{t})", Fore.LIGHTRED_EX + i + Style.RESET_ALL, end=e)
            elif i == "拆除卡":
                print(f"{t})", Fore.LIGHTGREEN_EX + i + Style.RESET_ALL, end=e)
            elif i == "特殊連擊":
                print(f"{t})", Fore.LIGHTRED_EX + i + Style.RESET_ALL, end=e)
            else:
                print(f"{t})", i, end=e)
            t += 1


def show(n):  #要看的人
    print(Fore.MAGENTA + f"玩家{n+1}:" + Style.RESET_ALL)
    print("--------------")
    color_print(player_deck[n],"\n")

print()

for num in range(0, len(player_deck)):  #開局看手牌(全部人)
    show(num)   
print("///////////////////////////////")
#牌已分發完畢 開始遊戲
"""
deck 牌庫
player_deck 玩家牌庫(只儲存玩家的卡牌)
player_num 總人數
turn 回合玩家索引#
card_num 卡牌索引
Accept 流程正確可使用
"""
turn = 0
turn_list = []
check_nope_list=[]
for i in range(player_num):
    turn_list.append(i)

show(turn)
used_list = []
attack_target = -1

def run(c, t):
    if c == "恩惠卡":
        message(c,t)
        while True:
            try:
                favor_player = int(input("選擇一個玩家:玩家"))
                if favor_player == t + 1 or (favor_player-1 not in turn_list):
                    raise
                break
            except:
                print("輸入錯誤玩家")
                continue
        show(favor_player - 1)
        while True:
            try:
                favor_card = int(input(f"選擇一張牌給玩家{t+1}:"))
                if favor_card > len(player_deck[favor_player - 1]):
                    raise
                break
            except:
                print("輸入錯誤索引")
                continue

        player_deck[t].append(player_deck[favor_player - 1][favor_card - 1])
        print(f"\n已給予-",end="")
        color_print(player_deck[favor_player-1][favor_card-1],"")
        input()
        del player_deck[favor_player - 1][favor_card - 1]

    elif c == "洗牌卡":
        message(c,t)
        random.shuffle(deck)

    elif c == "預知未來":
        message(c,t)
        print("\n接下來的三張為")
        color_print(deck[0:3], "\n")

    elif c == "拆除卡":
        message(c,t)

    elif c == "攻擊卡":
        global attack_time
        attack_time = 0
        message(c,t)
        while True:
            global attack_target
            if attack_target > turn_list[len(turn_list) - 1]:
                attack_target = turn_list[0]
                break
            elif attack_target not in turn_list or attack_target == t:
                attack_target = t + 1
                break
            elif attack_target in turn_list:
                break
        input(f"\n對下位玩家施放攻擊 下回合必須執行額外一回合!!!")

    if c=="特殊連擊":
        pass
    else:
        used_list.append(player_deck[t][player_deck[t].index(c)])
        del player_deck[t][player_deck[t].index(c)]

def special_combo(c,t):
    if len(c.split(" "))==2:
        c1,c2=map(int,c.split(" "))
        card_1=player_deck[t][c1-1]
        card_2=player_deck[t][c2-1]
        if card_1==card_2:
            input(Fore.LIGHTYELLOW_EX + "\n成雙成對"+Style.RESET_ALL)
            del player_deck[t][player_deck[t].index(card_1)]
            del player_deck[t][player_deck[t].index(card_2)]
            while True:
                try:
                    special_combo_player = int(input("想要誰給你牌呢:玩家"))
                    if special_combo_player == t + 1 or special_combo_player-1 not in turn_list:
                        raise
                    special_combo_player = special_combo_player-1
                    try:
                        ans=int(input(f"抽張牌(1~{len(player_deck[special_combo_player])})"))
                        if not 0<=ans<=len(player_deck[special_combo_player]):
                            raise
                        print("已給予-",end="")
                        color_print(player_deck[special_combo_player][ans-1],"")
                        input()
                        player_deck[t].append(player_deck[special_combo_player][ans-1])
                        del player_deck[special_combo_player][ans-1]
                        break
                    except:
                        print("輸入錯誤卡牌")
                        continue
                except:
                    print("輸入錯誤玩家")
                    continue
        else:
            return "error"
    elif len(c.split(" "))==3:
        c1,c2,c3=map(int,c.split(" "))
        card_1=player_deck[t][c1-1]
        card_2=player_deck[t][c2-1]
        card_3=player_deck[t][c3-1]
        if card_1==card_2==card_3:
            input(Fore.LIGHTYELLOW_EX +"\n三條"+Style.RESET_ALL)
            del player_deck[t][player_deck[t].index(card_1)]
            del player_deck[t][player_deck[t].index(card_2)]
            del player_deck[t][player_deck[t].index(card_3)]
            while True:
                try:
                    special_combo_player = int(input("想要誰給你牌呢:玩家"))
                    if special_combo_player == t + 1 or special_combo_player-1 not in turn_list:
                        raise
                    special_combo_player=special_combo_player-1
                    try:
                        ans=input(f"說出你想要甚麼牌?(沒有的話就沒機會囉~)")
                        if ans not in ["拆除卡","攻擊卡","預知未來","休想卡","跳過卡","恩惠卡","洗牌卡","瓜貓","毛茸茸馬鈴薯貓","嘔吐彩虹貓","塔可貓","鬍子貓"]:
                            print("輸入錯誤名稱")
                            continue
                        elif ans not in player_deck[special_combo_player]:
                            print("哎呀 沒有你想要的牌 機會沒拉!!!")
                            break
                        ans=player_deck[special_combo_player][player_deck[special_combo_player].index(ans)]
                        print("已給予-",end="")
                        color_print(ans,"")
                        input()
                        player_deck[t].append(ans)
                        del player_deck[special_combo_player][player_deck[special_combo_player].index(ans)]
                        break
                    except:
                        print("輸入錯誤卡牌")
                        continue
                except:
                    print("輸入錯誤玩家")
                    continue
        else:
            return "error"

    elif len(c.split(" "))==5:
        c_num=c.split(" ")
        c1=player_deck[t][int(c_num[0])-1]
        c2=player_deck[t][int(c_num[1])-1]
        c3=player_deck[t][int(c_num[2])-1]
        c4=player_deck[t][int(c_num[3])-1]
        c5=player_deck[t][int(c_num[4])-1]
        if c1!=c2!=c3!=c4!=c5:
            input(Fore.LIGHTYELLOW_EX +"\n5張卡牌面不同"+Style.RESET_ALL)
            print("\n棄牌區裡的卡牌有:",end="")
            for i in ["拆除卡","攻擊卡","預知未來","休想卡","跳過卡","恩惠卡","洗牌卡","瓜貓","毛茸茸馬鈴薯貓","嘔吐彩虹貓","塔可貓","鬍子貓"]:
                if used_list.count(i)>0:
                    color_print(i," | ")
            input()
            while True:
                special_ans=input("\n(從棄牌區選一張喜歡的牌吧!)\n[卡牌名稱]選卡 [A]放棄\n我想要:")
                if special_ans in used_list:
                    special_index=used_list.index(special_ans)
                    print("已給予-",end="")
                    color_print(used_list[special_index],"")
                    input()
                    player_deck[t].append(used_list[special_index])
                    del used_list[special_index]
                    del player_deck[t][player_deck[t].index(c1)]
                    del player_deck[t][player_deck[t].index(c2)]
                    del player_deck[t][player_deck[t].index(c3)]
                    del player_deck[t][player_deck[t].index(c4)]
                    del player_deck[t][player_deck[t].index(c5)]
                    break
                elif special_ans=="A" or special_ans=="a":
                    input(f"\n玩家{t+1}放棄了特殊連擊!!!")
                    break
                else:
                    print("哎呀 沒有你想要的牌(可以放棄)")
                    continue
        else:
            return "error"
    else:
        return "error"
print("[A]抽牌 [B]查看手牌 [C]特殊連擊 [D]查看牌庫量 [數字]出牌")
def gaming(turn):
    while True:
        global card,turn_list
        try:
            card_num = input(f"\n玩家{turn+1}:我想要")  #12345
            if card_num == "A" or card_num == "a":
                if not len(deck)>0:
                    print("\n牌庫沒拉!!!")
                    continue
                card = ""
                break

            elif card_num == "B" or card_num == "b":
                show(turn)
                raise IndexError

            elif card_num=="":
                raise IndexError

            elif card_num=="C" or card_num=="c":
                n=input("輸入連擊(Ex:1 2 3):")
                
            elif card_num=="D" or card_num=="d":
                input(f"\n現在牌庫量: {len(deck)} 張")
                continue
                
            elif card_num not in [str(i) for i in range(1,len(player_deck[turn])+1)]:
                raise IndexError
            
            if  card_num=="C" or card_num=="c":
                card="特殊連擊"
            else:
                card_num = int(card_num)
                card = player_deck[turn][card_num - 1]
                if not (0 < card_num <= len(player_deck[turn]) and card != "休想卡" and card != "拆除卡"):
                    raise IndexError
            check_nope_list =[0,1,2,3]
            check_nope=False
            for i in check_nope_list:
                if i not in turn_list:
                    check_nope_list.remove(i)
            if turn in check_nope_list:   
                check_nope_list.remove(turn)
            for i in check_nope_list:
                if "休想卡" in player_deck[i]:
                    check_nope=True
                    break
            if check_nope==True:
                while True:
                    print(f"\n玩家{turn+1} 要施放 ",end="")
                    color_print(card," !!!")
                    input()
                    try:
                        ask_want_to_draw = input("\n在我們之中有人擁有休想卡\n輸入玩家名稱即可禁止他:玩家")
                        try:
                            ask_want_to_draw = int(ask_want_to_draw)
                        except:
                            ask_want_to_draw = -1
                        if ask_want_to_draw -1 in check_nope_list:
                            if  "休想卡" in player_deck[ask_want_to_draw-1] and ask_want_to_draw - 1 != turn:
                                Skip_index = player_deck[ask_want_to_draw -1].index("休想卡")
                                input("\n\"休想!!!\"")
                                del player_deck[ask_want_to_draw - 1][Skip_index]
                                del player_deck[turn][card_num-1]
                                if "休想卡" in player_deck[turn]:
                                    ans=input("\n(你擁有休想卡 是否休想他的休想!!\n[A]休想休想我!! [任意]放棄")
                                    if ans=="A" or ans=="a":
                                        input(f"\n(此時玩家{turn+1}露出了一抹微笑...)")
                                        input("\n\"休想休想我!!!\"")
                                        used_list.append(player_deck[turn][player_deck[turn].index("休想卡")])
                                        del player_deck[turn][player_deck[turn].index("休想卡")]
                                        raise CheckNopeException
                                    else:
                                        input("\n\"可惡!\"")
                                        used_list.append(player_deck[ask_want_to_draw - 1][Skip_index])                      
                                raise IndexError
                            elif ask_want_to_draw -1 == turn:
                                input("\n輸入錯誤")
                                continue
                            else:
                                raise CheckNopeException
                        else:
                            raise CheckNopeException

                    except CheckNopeException:
                        if card == "跳過卡":
                            used_list.append(player_deck[turn][player_deck[turn].index(card)])
                            del player_deck[turn][player_deck[turn].index(card)]
                            message(card,turn)
                            input("(跳過")
                            raise SkipException

                        elif card == "攻擊卡":
                            run(card, turn)
                            print("攻擊卡效果 不須抽卡!")
                            raise SkipException

                        elif card in ["塔可貓","毛茸茸馬鈴薯貓","瓜貓","鬍子貓","嘔吐彩虹貓"]:
                            if card == "塔可貓":
                                input("\n\"這是什麼味道?\"")

                            elif card == "毛茸茸馬鈴薯貓":
                                input("\n\"毛茸茸的馬鈴薯\"")

                            elif card == "瓜貓":
                                input("\n\"瓜!\"")

                            elif card == "鬍子貓":
                                input("\n\"好柔順的毛髮\"")

                            elif card == "R嘔吐彩虹貓":
                                input("\n\"嘔嘔嘔...(吐彩虹)\"")
                            used_list.append(player_deck[turn][player_deck[turn].index(card)])
                            del player_deck[turn][player_deck[turn].index(card)]
                            raise IndexError

                        elif card == "特殊連擊":
                            check_special_combo=special_combo(n,turn)
                            if check_special_combo=="error":
                                ans=input("\n輸入錯誤 無法連擊")
                            raise IndexError
                        else:
                            run(card, turn)
                            raise IndexError
            else:
                print("\n沒有人能夠阻止你!執行 ",end="")
                color_print(card,"")
                input()
                if card == "跳過卡":
                    used_list.append(player_deck[turn][player_deck[turn].index(card)])
                    message(card,turn)
                    input("(跳過\n")
                    del player_deck[turn][player_deck[turn].index(card)]
                    raise SkipException

                elif card == "攻擊卡":
                    run(card, turn)
                    input("攻擊卡效果 不須抽卡!")
                    raise SkipException

                elif card in ["塔可貓","毛茸茸馬鈴薯貓","瓜貓","鬍子貓","嘔吐彩虹貓"]:
                    if card == "塔可貓":
                        input("\n\"這是什麼味道?\"")

                    elif card == "毛茸茸馬鈴薯貓":
                        input("\n\"毛茸茸的馬鈴薯\"")

                    elif card == "瓜貓":
                        input("\n\"瓜!\"")

                    elif card == "鬍子貓":
                        input("\n\"好柔順的毛髮\"")

                    elif card == "嘔吐彩虹貓":
                        input("\n\"嘔嘔嘔...(吐彩虹)\"")
                    used_list.append(player_deck[turn][player_deck[turn].index(card)])
                    del player_deck[turn][player_deck[turn].index(card)]
                    raise IndexError
                    
                elif card == "特殊連擊":
                    check_special_combo=special_combo(n,turn)
                    if check_special_combo=="error":
                        ans=input("\n輸入錯誤 無法連擊")
                    raise IndexError
                else:
                    run(card, turn)
                    raise IndexError
            
        except IndexError:
            continue
        except SkipException:
            break


while player_num != 1:
    #完整一回合
    gaming(turn)
    if card != "跳過卡" and card != "攻擊卡":
        final = draw(1)
        if final == "Explode kitten":
            final = "爆炸貓"
        print(f"\n玩家{turn+1}抽到的是 ",end="")
        color_print(final,"\n")
    else:
        final = ""

    if final == "爆炸貓":
        if "拆除卡" in player_deck[turn]:
            message("拆除卡",turn)
            while True:
                try:
                    explode_index = int(input(f"快把爆炸貓小心翼翼地放回去!他很生氣!!!\n請把牠放在任何一處(0~{len(deck)-1})"))
                    if  not 0 <= explode_index <= len(deck)-1:
                        input("這地方容不下脆弱的牠")
                        continue
                    message("Put Explode kitten",turn)
                    deck.insert(explode_index,"Explode kitten")
                    used_list.append(player_deck[turn][player_deck[turn].index("拆除卡")])
                    del player_deck[turn][player_deck[turn].index("拆除卡")]
                    break
                except:
                    print("輸入錯誤!")
                    continue
        else:
            message(final,turn)
            input(f"你輸了!玩家{turn+1}")
            player_num -= 1
            turn_list.remove(turn)
    else:
        player_deck[turn].append(final)
    
    if attack_target == turn and attack_time != 1:
        input("\n攻擊卡成效!")
        attack_target += 1
        attack_time = attack_time + 1
        continue

    while len(turn_list) != 1:
        turn += 1
        if turn > turn_list[len(turn_list) - 1]:
            turn = turn_list[0]
            break
        elif turn not in turn_list:
            while turn not in turn_list:
                turn += 1
            break
        elif turn in turn_list:
            break
            
cls()
turn_list[0] = turn_list[0] + 1 
talk("\n\"咚咚咚咚咚...(打鼓聲\"")  
talk("\n\"在這場刺激的炸彈貓遊戲裡的最終贏家是...\"")   
print("\n贏家是{}".format(turn_list))
input(Fore.LIGHTRED_EX + "Congratulations!" + Style.RESET_ALL)