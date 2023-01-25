import random
import colorama
from colorama import Fore, Style
"""
ver2.0
完成:
    基本功能
    攻擊卡
新增:    
    debug
    修正貓咪卡
未來:
    特殊連擊
    對話
"""

class IndexError(Exception):
  pass


class SkipException(Exception):
  pass


class CheckNopeException(Exception):
  pass


global deck, used_list
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
    player_num = int(input("人數"))
    if not 1 < player_num < 6:
      raise
    break
  except:
    print("請輸入正確人數(2~4)")
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
    l = [l]
  t = 1
  for i in l:
    if i == "Attack":
      print(f"{t})", Fore.RED + i + Style.RESET_ALL, end=e)
    elif i == "Favor":
      print(f"{t})", Fore.LIGHTYELLOW_EX + i + Style.RESET_ALL, end=e)
    elif i == "Shuffle":
      print(f"{t})", Fore.LIGHTBLUE_EX + i + Style.RESET_ALL, end=e)
    elif i == "Skip":
      print(f"{t})", Fore.LIGHTRED_EX + i + Style.RESET_ALL, end=e)
    elif i == "Nope":
      print(f"{t})", Fore.LIGHTBLACK_EX + i + Style.RESET_ALL, end=e)
    elif i == "See the future":
      print(f"{t})", Fore.LIGHTMAGENTA_EX + i + Style.RESET_ALL, end=e)
    elif i == "Exploding cat":
      print(f"{t})", Fore.LIGHTRED_EX + i + Style.RESET_ALL, end=e)
    elif i == "Defuse":
      print(f"{t})", Fore.LIGHTGREEN_EX + i + Style.RESET_ALL, end=e)
    else:
      print(f"{t})", i, end=e)
    t += 1
  print()


def show(n):  #要看的人
  print(Fore.MAGENTA + f"Player{n+1}:" + Style.RESET_ALL)
  print("--------------")
  color_print(player_deck[n], "\n")


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
for i in range(player_num):
  turn_list.append(i)

show(turn)
used_list = []
attack_target = -1


def run(c, t):
  used_list.append(c)
  if c == "Favor":
    while True:
      try:
        favor_player = int(input("選擇一個玩家:P"))
        if favor_player == t + 1 or favor_player not in turn_list:
          raise
        break
      except:
        print("輸入錯誤玩家")
        continue
    show(favor_player - 1)
    while True:
      try:
        favor_card = int(input("Choose a card you want to give"))
        if favor_card > len(player_deck[favor_player - 1]):
          raise
        break
      except:
        print("輸入錯誤索引")
        continue

    player_deck[t].append(player_deck[favor_player - 1][favor_card - 1])
    print(f"已給予-{player_deck[favor_player-1][favor_card-1]}")
    del player_deck[favor_player - 1][favor_card - 1]

  elif c == "Shuffle":
    print("\n洗牌中")
    random.shuffle(deck)

  elif c == "See the future":
    print("\n接下來的三張為")
    color_print(deck[0:3], "\n")

  elif c == "Defuse":
    print("拆除炸彈!")

  elif c == "Attack":
    global attack_time
    attack_time = 0
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
      print(f"對Player{t+2}施放攻擊卡!下回合必須執行額外一回合!")

  del player_deck[t][player_deck[t].index(c)]

print(f"現在牌庫量: {len(deck)} 張")
def gaming(turn):
  while True:
    global card
    try:
      card_num = input(f"Player{turn+1}請出牌:")  #12345
      if card_num == "抽牌":
        if not len(deck)>0:
          print("\n牌庫沒拉!!!")
          continue
        card = ""
        break
      elif card_num == "我要看手牌":
        show(turn)
        raise IndexError("輸入錯誤")
      elif card_num=="":
        raise IndexError("輸入錯誤")
      elif card_num not in [str(i) for i in range(1,len(player_deck[turn])+1)]:
        raise IndexError()
      card_num = int(card_num)
      card = player_deck[turn][card_num - 1]
      if 0 < card_num < len(
          player_deck[turn]) and card != "Nope" and card != "Defuse":  #卡牌索引正確
        check_nope_list = turn_list
        if turn in check_nope_list:
          check_nope_list.remove(turn)
        else:
          pass
        for i in check_nope_list:
          if "Nope" in player_deck[i]:  #除了本回合玩家以外的人只要有nope 斷迴圈開始詢問
            while True:
              print(f"Player{turn+1} 要施放 {card} !!!")
              try:
                ask_want_to_draw = input("我們之中有禁止卡\n若不想出牌請輸入任何字元")
                try:
                  ask_want_to_draw = int(ask_want_to_draw)
                except:
                  ask_want_to_draw = -1
                if ask_want_to_draw - 1 in turn_list:

                  if ask_want_to_draw - 1 in turn_list and ask_want_to_draw - 1 != turn:
                    Skip_index = player_deck[ask_want_to_draw -1].index("Nope")
                    print("休想!!!")
                    del player_deck[ask_want_to_draw - 1][Skip_index]
                    raise IndexError
                  elif ask_want_to_draw - 1 == turn:
                    print("\n輸入錯誤")
                    continue
                  else:
                    raise CheckNopeException
                else:
                  raise CheckNopeException

              except CheckNopeException:
                print("\n沒人要禁止 執行")
                if card == "Skip":
                  del player_deck[turn][player_deck[turn].index(card)]
                  print("跳過")
                  raise SkipException
                elif card == "Attack":
                  run(card, turn)
                  print("攻擊卡效果 不須抽卡!")
                  raise SkipException
                else:
                  run(card, turn)
                  raise IndexError()
          else:
            if card == "Skip":
              del player_deck[turn][player_deck[turn].index(card)]
              print("跳過")
              raise SkipException
            else:
              run(card, turn)
              raise IndexError()
      else:
        print("索引錯誤")
        raise IndexError("輸入的數字索引值錯誤")
    except IndexError:
      print(f"還是Player{turn+1}的回合!!!")
      continue
    except SkipException:
      break


while player_num != 1:
  #完整一回合
  gaming(turn)
  if card != "Skip" and card != "Attack":
    final = draw(1)
    print(f"Player{turn+1}抽到的是", end="")
    color_print(final, "")
  else:
    final = ""

  if final == "Explode kitten":
    if "Defuse" in player_deck[turn]:
      print("拆除炸彈成功!!!")
      while True:
        explode_index = int(input(f"你免於爆炸貓的洗禮 請把牠放在任何一處(0~{len(deck)-1})"))
        if 0>=explode_index>len(deck)-1:
          print("放錯啦!!!")
          continue
      deck.insert(explode_index,"Explode kitten")
      del player_deck[turn][player_deck[turn].index("Defuse")]
    else:
      print(f"你輸了!Player{turn+1}")
      player_num -= 1
      turn_list.remove(turn)
  else:
    player_deck[turn].append(final)
    
  if attack_target == turn and attack_time != 1:
    print("攻擊卡成效!")
    attack_target += 1
    attack_time = attack_time + 1
    continue

  while len(turn_list) != 1:
    turn += 1
    if turn > turn_list[len(turn_list) - 1]:
      turn = turn_list[0]
      break
    elif turn not in turn_list:
      while turn not in turn:
        turn += 1
      break
    elif turn in turn_list:
      break

turn_list[0] = turn_list[0] + 1
print("贏家是{}".format(turn_list))