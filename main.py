# 1. Print logo
# 2. print A vs B
# 3. compare Who has more followers? Type 'A' or 'B': 
# 4. If correct guess then increase the scroe. You're right! Current score: 1.
# 5. If wrong end the game show score 
from art import logo, vs
from game_data import data
from replit import clear
from random import choice

# print(logo)
# input()
# print(vs)
# input()
# print(data)
# clear()

def screenDisplay(myText, score, isFinal,isFirst):
  clear()
  if isFinal:
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
  elif isFirst:
    print(logo)
    print(myText)
  else:
    print(logo)
    print(f"You're right! Current score: {score}")
    print(myText)


def getChoice():
  return choice(data),choice(data)


isFirst = True
isFinal = False
score = 0

while not isFinal:
  a,b = getChoice()
  txt = f"Compare A: {a['name']}, a {a['description']}, from {a['country']}. {vs} Compare B: {b['name']}, a {b['description']}, from {b['country']}"
  if isFirst:
    screenDisplay(txt,0,False,True)
    option = input("Who has more followers? Type 'A' or 'B':").lower()
    if option == "a" and a['follower_count'] > b['follower_count']:
      score += 1
      isFirst = False
      print(f"a: {a['follower_count']} and b: {b['follower_count']}")
    elif option == "b" and a['follower_count'] < b['follower_count']:
      score += 1
      isFirst = False
      print(f"a: {a['follower_count']} and b: {b['follower_count']}")
    else:
      screenDisplay("",score,True,False)
      isFinal = True
      print(f"a: {a['follower_count']} and b: {b['follower_count']}")
  else:
    screenDisplay(txt,score,False,False)
    option = input("Who has more followers? Type 'A' or 'B':").lower()
    if option == "a" and a['follower_count'] > b['follower_count']:
      score += 1
      isFirst = False
      print(f"a: {a['follower_count']} and b: {b['follower_count']}")
    elif option == "b" and a['follower_count'] < b['follower_count']:
      score += 1
      isFirst = False
      print(f"a: {a['follower_count']} and b: {b['follower_count']}")
    else:
      screenDisplay("",score,True,False)
      isFinal = True
      print(f"a: {a['follower_count']} and b: {b['follower_count']}")
      










# isF = False


# while not isF:
#   print(logo)
#   choiceA = choice(data)
#   choiceB = choice(data)
#   print(choiceA)
#   print(choiceB)
#   if choiceA == choiceB:
#     print("Yes")









