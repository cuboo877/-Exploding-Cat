import random
import colorama
from colorama import Fore, Style
import time

class IndexError(Exception):
    pass
class SkipException(Exception):
    pass
class CheckNopeException(Exception):
    pass

def talk(n):
    for i in n:
        print(i,end="")
        time.sleep(0.1)
    print()

global used_list,deck
deck = []
for i in range(4):
    #deck.append("Explode kitten")
    deck.append("Attack")
    deck.append("Favor")
    deck.append("Shuffle")
    deck.append("Skip")
for i in range(5):
    deck.append("Nope")
    deck.append("See the future")
for i in range(4):
    deck.append("TacoCat")
    deck.append("Hairy Potato Cat")
    deck.append("Cattermellon")
    deck.append("Beard Cat")
    deck.append("Rainbow-Ralphing Cat")
random.shuffle(deck)

"""
抽卡函式 參數=張
全域 玩家卡牌庫
運行num次
回傳 玩家卡牌庫
"""
def plot():
    def restart():
        input("-Have you ever wondered why the Titanic sank?\n")
        input("-No... not a corny dirty joke\n")
        input("-In fact, it sank because the cat made trouble on the boat!\n")
        input("-Don't believe it? You will believe it after playing this game~\n")
        input("Explain the rules?\n")
        input("-This game supports 2~5 people\n")
        input(" Here is a simple tutorial. The rules of the game are super super simple!\n")
        input("-Before The Game Start:")
        print(" 1. To start, remove all the Exploding Kittens(4) from the deck and set them aside.")
        print(" 2. Remove all of the Defuse Cards(6) from the deck and deal 1 to each player.")
        print(" 3. Insert the extra Defuse Cards back in the deck.")
        print(" 4. Let's play !!!\n")
    def start_rule():
        input("-Game Start:\n")
        input(" Take your turn:\n")
        input(" 1.Pass:Play no card.\n")
        input(" 2.Play:Play a card and following the instructions on the card.\nBtw, You can play as many cards as you'd like.\n")
        input(" You need to draw a card if your turn is over \n")
        input("-if you explode?\n")
        input(" BOOOOOOOOM\n")
        input(" You lose the game\n")
        input(" This process continues until there's only 1 player left, who wins the game.\n")
        input("-Congratulations! You are alive!\n")
    def special_card_rule():
        input("-Field Guide\n")
        input("-Explode kitten:\n You must show this card immediately. Unless you have a Defuse Card, you're dead. Discard all of your cards, including the Exploding Kitten.\n")
        input("-See the future:\n Privately view the top 3 cards from the Draw Pile and put them back in the same order.\n Don't show the cards to the other players.\n")
        input("-Skip:\n If you play a Skip Card as a defense to an Attack Card, it only ends 1 of the 2 turns. 2 Skip Cards would end both turns.\n(Immediately end your turn without drawing a card.)\n")
        input("-Shuffle:\n Shuffle the Draw Pile thoroughly. (Useful when you know there's an Exploding Kitten coming.)\n")
        input("-Attack:\n Do not draw any cards. Instead, immediately force the next player to take 2 turns in a row. Play then continues from that player.\n The victim of this card takes a turn as normal (play-or-pass then draw). Then, when their first turn is over, it's their turn again.\n")
        input("-Favor:\n Force any other player to give you 1 card from their hand. They choose which card to give you.\n")
        input("-Defuse:\n Want to hurt the player right after you? Put the Kitten right on top of the deck. If you'd like, hold the deck under the table so that no one else can see where you put it.\n")
        input("-Nope:\n Stop any action except for an Exploding Kitten or a Defuse Card.\n Imagine that any card beneath a Nope Card never existed.\n")
        input("-Cat cards:\n These cards are powerless on their own, but if you collect any 2 matching Cat Cards\n you can play them as a Pair to steal a random card from any player.\n")
        input("-Other Rule:\n")
        input(" 1.If the victim of an Attack Card plays an Attack Card on any of their turns, the new target must take any remaining turns plus the number of attacks on the Attack Card just played\n (e.g. 4 turns, then 6, and so on).\n")
        input(" 2.A Nope can also be played on another Nope to negate it and create a Yup, and so on.\n You can even play a Nope on a SPECIAL COMBO.")
    def special_combo_rule():
        input("-Special Combos:\n")
        input(" Two of a Kind:\n Playing matching Pairs of Cat Cards (where you get to steal a random card from another player) no longer only applies to pairs of Cat Cards. It now applies to ANY pair of cards with the same title\n")
        input(" Three of a Kind:\n When you play 3 matching cards (any 3 cards with the same title), you get to pick a player and name a card.\n If they have that card, they must give one to you. If they don't have it, you get nothing. Ignore the instructions on the cards when you play a combo.\n")
        input(" Five of different kind:\n If you have 5 cards with different titles when you are in trouble, put those cards in the drop zone and take a card of your choice from the drop zone\n")

    restart()
    start_rule()
    special_card_rule()
    special_combo_rule()
    while True:
        ans=input("\"Meow??\"(Are you READY???)\n[Any]Start / [R]Restart the rule / [1]Basic rule / [2]Field guide / [3]Special combos\n")
        if ans=="R" or ans=="r":
            plot()
        elif ans=="1":
            start_rule()
        elif ans=="2":
            special_card_rule()
        elif ans=="3":
            special_combo_rule()
        else:
            break
print("-First play???")
start_plot=input("[Any]Start [N]I want to know how to play this game")
if start_plot=="N" or start_plot=="n":
    print()
    plot()
else:
    print()
    pass

def message(kind,t):
    t=t+1
    if kind=="Explode kitten":
        talk("\n\"Ssssssss......\"")
        input()
        input("(Boom\n")
        a=input("\"Say goodbye to the world, by the way, damn cat\"")

    elif kind=="Defuse":
        talk("\n\"hiss......\"")
        input()
        input("(click!\n")

    elif kind=="Put Explode kitten":
        input("\n\"I saw your smirk, did you put the cat in the first picture?\"")

    elif kind=="See the future":
        input("\n\"Actually you just want to know tomorrow's lotto numbers\"")

    elif kind=="Attack":
        input(f"\n\"The timing of this shot is usually that the opponent already knows that there is a bomb cat in the future, so fight back as soon as possible!!\"")

    elif kind=="Favor":
        l=["\n\"It's not stealing, it's good people get good rewards\"","\n\"Thank you for your card even though I know you're reluctant to give it to me\""]
        input(random.choice(l))
    
    elif kind=="Skip":
        input("\n\"When you saw the Explode cat, you ran away~\"")

    elif kind=="Shuffle":
        l=["\n\"Please remember to say stop! Shuffled to hand cramps\"","\n\"The saddest moment in my life, it is still Explode cat\""]
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


global player_deck, player_num, turn
player_deck = []
while True:
    try:
        player_num = int(input("How many people here?:"))
        if not 1 < player_num < 6:
            raise
        break
    except:
        print("Please enter a right number(2~4)")
        continue

for i in range(player_num):
    player_deck.append(draw(7))
for num in range(0, player_num):
    player_deck[num].append("Defuse")
for i in range(player_num - 1):
    deck.append("Explode kitten")
for i in range(6 - player_num):
    deck.append("Defuse")  #炸彈貓 拆彈卡放回去

for i in range(5):
    random.shuffle(deck)  #洗5次牌
"""
看手牌函式
show(玩家索引12345):
"""


def color_print(l, e):
    if type(l) != list:
        if l == "Attack":
            print(Fore.RED + l + Style.RESET_ALL, end=e)
        elif l == "Favor":
            print(Fore.LIGHTYELLOW_EX + l + Style.RESET_ALL, end=e)
        elif l == "Shuffle":
            print(Fore.LIGHTBLUE_EX + l + Style.RESET_ALL, end=e)
        elif l == "Skip":
            print(Fore.LIGHTCYAN_EX + l + Style.RESET_ALL, end=e)
        elif l == "Nope":
            print(Fore.LIGHTBLACK_EX + l + Style.RESET_ALL, end=e)
        elif l == "See the future":
            print(Fore.LIGHTMAGENTA_EX + l + Style.RESET_ALL, end=e)
        elif l == "Explode kitten":
            print(Fore.LIGHTRED_EX + l + Style.RESET_ALL, end=e)
        elif l == "Defuse":
            print(Fore.LIGHTGREEN_EX + l + Style.RESET_ALL, end=e)
        elif l == "Special Combos":
            print(Fore.LIGHTRED_EX + l + Style.RESET_ALL, end=e)
        else:
            print(l, end=e)
    else:
        t = 1
        for i in l:
            if i == "Attack":
                print(f"{t})", Fore.RED + i + Style.RESET_ALL, end=e)
            elif i == "Favor":
                print(f"{t})", Fore.LIGHTYELLOW_EX + i + Style.RESET_ALL, end=e)
            elif i == "Shuffle":
                print(f"{t})", Fore.LIGHTBLUE_EX + i + Style.RESET_ALL, end=e)
            elif i == "Skip":
                print(f"{t})", Fore.LIGHTCYAN_EX + i + Style.RESET_ALL, end=e)
            elif i == "Nope":
                print(f"{t})", Fore.LIGHTBLACK_EX + i + Style.RESET_ALL, end=e)
            elif i == "See the future":
                print(f"{t})", Fore.LIGHTMAGENTA_EX + i + Style.RESET_ALL, end=e)
            elif i == "Explode kitten":
                print(f"{t})", Fore.LIGHTRED_EX + i + Style.RESET_ALL, end=e)
            elif i == "Defuse":
                print(f"{t})", Fore.LIGHTGREEN_EX + i + Style.RESET_ALL, end=e)
            elif i == "Special Combos":
                print(f"{t})", Fore.LIGHTRED_EX + i + Style.RESET_ALL, end=e)
            else:
                print(f"{t})", i, end=e)
            t += 1


def show(n):  #要看的人
    print(Fore.MAGENTA + f"Player{n+1}:" + Style.RESET_ALL)
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
    if c == "Favor":
        message(c,t)
        while True:
            try:
                favor_player = int(input("Choose a player:P"))
                if favor_player == t + 1 or (favor_player-1 not in turn_list):
                    raise
                break
            except:
                print("Error player")
                continue
        show(favor_player - 1)
        while True:
            try:
                favor_card = int(input(f"Choose a card for the Player{t+1}:"))
                if favor_card > len(player_deck[favor_player - 1]):
                    raise
                break
            except:
                print("Index Error")
                continue

        player_deck[t].append(player_deck[favor_player - 1][favor_card - 1])
        print(f"\nGave-",end="")
        color_print(player_deck[favor_player-1][favor_card-1],"")
        input()
        del player_deck[favor_player - 1][favor_card - 1]

    elif c == "Shuffle":
        message(c,t)
        random.shuffle(deck)

    elif c == "See the future":
        message(c,t)
        print("\nThe next Three Step is:")
        color_print(deck[0:3], "\n")

    elif c == "Defuse":
        message(c,t)

    elif c == "Attack":
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
        input(f"\nCasting an attack on Player{t+2} must perform an extra round in the next round!!!")

    if c=="Special Combos":
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
            input(Fore.LIGHTYELLOW_EX +"\nTwo of Kind"+Style.RESET_ALL)
            del player_deck[t][player_deck[t].index(card_1)]
            del player_deck[t][player_deck[t].index(card_2)]
            while True:
                try:
                    special_combo_player = int(input("Who do you want to give you a card?:P"))
                    if special_combo_player == t + 1 or special_combo_player-1 not in turn_list:
                        raise
                    special_combo_player=special_combo_player-1
                    try:
                        ans=int(input(f"Draw a card(1~{len(player_deck[special_combo_player])})"))
                        if not 0<=ans<len(player_deck[special_combo_player]):
                            raise
                        print("Gave-",end="")
                        color_print(player_deck[special_combo_player][ans-1],"")
                        input()
                        player_deck[t].append(player_deck[special_combo_player][ans-1])
                        del player_deck[special_combo_player][ans-1]
                        break
                    except:
                        print("Error card")
                        continue
                except:
                    print("Error player")
                    continue
        else:
            return "error"
    elif len(c.split(" "))==3:
        c1,c2,c3=map(int,c.split(" "))
        card_1=player_deck[t][c1-1]
        card_2=player_deck[t][c2-1]
        card_3=player_deck[t][c3-1]
        if card_1==card_2==card_3:
            input(Fore.LIGHTYELLOW_EX +"\nThree of Kind"+Style.RESET_ALL)
            del player_deck[t][player_deck[t].index(card_1)]
            del player_deck[t][player_deck[t].index(card_2)]
            del player_deck[t][player_deck[t].index(card_3)]
            while True:
                try:
                    special_combo_player = int(input("Who want to give you cards :P"))
                    if special_combo_player == t + 1 or special_combo_player-1 not in turn_list:
                        raise
                    special_combo_player=special_combo_player-1
                    try:
                        ans=input(f"Say what card you want? (If you don't have it, you won't have another chance~)")
                        if ans not in ["Defuse","Attack","See the future","Nope","Skip","Favor","Shuffle","Cattermellon","Hairy Potato Cat","Rainbow-Ralphing Cat","TacoCat","Bread Cat"]:
                            print("Error Name")
                            continue
                        elif ans not in player_deck[special_combo_player]:
                            print("Oops, there is no card you want")
                            break
                        ans=player_deck[special_combo_player][player_deck[special_combo_player].index(ans)]
                        print("Gave-",end="")
                        color_print(ans,"")
                        input()
                        player_deck[t].append(ans)
                        del player_deck[special_combo_player][player_deck[special_combo_player].index(ans)]
                        break
                    except:
                        print("Error Card")
                        continue
                except:
                    print("Error Player")
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
            input(Fore.LIGHTYELLOW_EX +"\nFive of different kind"+Style.RESET_ALL)
            print("\nThe cards in the discard pile are:",end="")
            for i in ["Defuse","Attack","See the future","Nope","Skip","Favor","Shuffle","Cattermellon","Hairy Potato Cat","Rainbow-Ralphing Cat","TacoCat","Bread Cat"]:
                if used_list.count(i)>0:
                    color_print(i," | ")
            input()
            while True:
                special_ans=input("\n(Choose a card you like from the discard pile!)\n[Name]Play [A]Give up\n")
                if special_ans in used_list:
                    special_index=used_list.index(special_ans)
                    print("Gave-",end="")
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
                    input(f"\nPlayer{t+1}Abandoned Special Combo!!!")
                    break
                else:
                    print("Oops, no cards you want.")
                    continue
        else:
            return "error"
    else:
        return "error"
        
print(f"\nNumber of Deck: {len(deck)}\n")
print("[A]Draw [B]Check my hand [C]Special Combos [D]Check the number of Deck [Number]Play")
def gaming(turn):
    while True:
        global card,turn_list
        try:
            card_num = input(f"\nPlayer{turn+1}:I want ")  #12345
            if card_num == "A" or card_num == "a":
                if not len(deck)>0:
                    print("\nNo card")
                    continue
                card = ""
                break

            elif card_num == "B" or card_num == "b":
                show(turn)
                raise IndexError

            elif card_num=="":
                raise IndexError

            elif card_num=="C" or card_num=="c":
                n=input("Enter Combos(Ex:1 2 3):")
                
            elif card_num=="D" or card_num=="d":
                input(f"\nNumber of Deck: {len(deck)}")
                continue
                
            elif card_num not in [str(i) for i in range(1,len(player_deck[turn])+1)]:
                raise IndexError
            
            if  card_num=="C" or card_num=="c":
                card="Special Combos"
            else:
                card_num = int(card_num)
                card = player_deck[turn][card_num - 1]
                if not (0 < card_num <= len(player_deck[turn]) and card != "Nope" and card != "Defuse"):
                    raise IndexError
            check_nope_list = turn_list
            check_nope=False
            if turn in check_nope_list:  
                turn_list=turn_list    
                del check_nope_list[check_nope_list.index(turn)]
            for i in check_nope_list:
                if "Nope" in player_deck[i]:
                    check_nope=True
                    break
            if check_nope==True:
                while True:
                    print(f"\nPlayer{turn+1} want ot play ",end="")
                    color_print(card," !!!")
                    input()
                    try:
                        ask_want_to_draw = input("\nSome of us have a Nope card\nEnter the player name to Stop him :P")
                        try:
                            ask_want_to_draw = int(ask_want_to_draw)
                        except:
                            ask_want_to_draw = -1
                        if ask_want_to_draw -1 in check_nope_list:
                            if  "Nope" in player_deck[ask_want_to_draw-1] and ask_want_to_draw - 1 != turn:
                                Skip_index = player_deck[ask_want_to_draw -1].index("Nope")
                                input("\n\"Nope!!!\"")
                                del player_deck[ask_want_to_draw - 1][Skip_index]
                                if "Nope" in player_deck[turn]:
                                    ans=input("\n(You have Nope card, Nope his Nope?\n[A]Nope!!! [Any]Give up")
                                    if ans=="A" or ans=="a":
                                        input("\n\"Nope to Nope me!!!\"")
                                        used_list.append(player_deck[turn][player_deck[turn].index("Nope")])
                                        del player_deck[turn][player_deck[turn].index("Nope")]
                                        raise CheckNopeException
                                    else:
                                        input("\n\"Damn!\"")
                                        used_list.append(player_deck[ask_want_to_draw - 1][Skip_index])                      
                                raise IndexError
                            elif ask_want_to_draw -1 == turn:
                                input("\nError")
                                continue
                            else:
                                raise CheckNopeException
                        else:
                            raise CheckNopeException

                    except CheckNopeException:
                        if card == "Skip":
                            used_list.append(player_deck[turn][player_deck[turn].index(card)])
                            del player_deck[turn][player_deck[turn].index(card)]
                            message(card,turn)
                            input("(Skip")
                            raise SkipException

                        elif card == "Attack":
                            run(card, turn)
                            print("Attack card effect No need to draw cards!")
                            raise SkipException

                        elif card in ["TacoCat","Hairy Potato Cat","Cattermellon","Beard Cat","Rainbow-Ralphing Cat"]:
                            if card == "TacoCat":
                                input("\n\"What does it taste like?\"")

                            elif card == "Hairy Potato Cat":
                                input("\n\"Fluffy potato\"")

                            elif card == "Cattermellon":
                                input("\n\"Yummy!\"")

                            elif card == "Beard Cat":
                                input("\n\"Very smooth hair\"")

                            elif card == "Rainbow-Ralphing Cat":
                                input("\n\"(vomit sound)\"")
                            used_list.append(player_deck[turn][player_deck[turn].index(card)])
                            del player_deck[turn][player_deck[turn].index(card)]
                            raise IndexError

                        elif card == "Special Combos":
                            check_special_combo=special_combo(n,turn)
                            if check_special_combo=="error":
                                ans=input("\nEnter Error Combos")
                            raise IndexError
                        else:
                            run(card, turn)
                            raise IndexError
            else:
                print("\nNobody can prevent you!",end="")
                color_print(card,"")
                input()
                if card == "Skip":
                    used_list.append(player_deck[turn][player_deck[turn].index(card)])
                    message(card,turn)
                    input("(Skip\n")
                    del player_deck[turn][player_deck[turn].index(card)]
                    raise SkipException

                elif card == "Attack":
                    run(card, turn)
                    input("Attack card effect No need to draw cards!")
                    raise SkipException

                elif card in ["TacoCat","Hairy Potato Cat","Cattermellon","Beard Cat","Rainbow-Ralphing Cat"]:
                    if card == "TacoCat":
                        input("\n\"What does it taste like?\"")

                    elif card == "Hairy Potato Cat":
                        input("\n\"Fluffy potato\"")

                    elif card == "Cattermellon":
                        input("\n\"Yummy!\"")

                    elif card == "Beard Cat":
                        input("\n\"Very smooth hair\"")

                    elif card == "Rainbow-Ralphing Cat":
                        input("\n\"(vomit sound)\"")
                    used_list.append(player_deck[turn][player_deck[turn].index(card)])
                    del player_deck[turn][player_deck[turn].index(card)]
                    raise IndexError
                    
                elif card == "Special Combos":
                    check_special_combo=special_combo(n,turn)
                    if check_special_combo=="error":
                        ans=input("\nEnter Error Combos")
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
    if card != "Skip" and card != "Attack":
        final = draw(1)
        print(f"\nPlayer{turn+1} Got: ",end="")
        color_print(final,"\n")
    else:
        final = ""

    if final == "Explode kitten":
        if "Defuse" in player_deck[turn]:
            message("Defuse",turn)
            while True:
                try:
                    explode_index = int(input(f"Put the Explode cat back carefully! He's angry!!!\nPlease put it anywhere(0~{len(deck)-1})"))
                    if not  0<=explode_index<=len(deck)-1:
                        print("There is no room for fragile it in this place")
                        continue
                    message("Put Explode kitten",turn)
                    deck.insert(explode_index,"Explode kitten")
                    used_list.append(player_deck[turn][player_deck[turn].index("Defuse")])
                    del player_deck[turn][player_deck[turn].index("Defuse")]
                    break
                except:
                    print("Enter Error!")
                    continue
        else:
            message(final,turn)
            input(f"You lose!Player{turn+1}")
            player_num -= 1
            turn_list.remove(turn)
    else:
        player_deck[turn].append(final)
    
    if attack_target == turn and attack_time != 1:
        input("\nAttack Card Works!")
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
    
turn_list[0] = turn_list[0] + 1     
print("Winner is {}".format(turn_list))     