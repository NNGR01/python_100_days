import random



def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)  

def compare(user_score, computer_score):
  if user_score == computer_score:
    return " Its Draw"
  elif computer_score == 0:
    return " Computer Black Jack"
  elif user_score == 0:
    return " User black Jack"
  elif user_score > 21:
    return " You lose"
  elif computer_score > 21:
    return " You win opponent went over"
  elif user_score > computer_score:
    return " You win "
  else:
    return " You lose"

def the_game(): 

  print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   )
  user_cards = []
  computer_cards = []
  the_game_over = False
      
  
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not the_game_over:
  
    user_score = calculate_score(user_cards)    
    computer_score = calculate_score(computer_cards)
    print(f" Yours cards : {user_cards}, current score : {user_score}")
    print(f" Computer's first card : {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      the_game_over = True
    else:
      another_card = input("Do you want another card? 'y' for yes, 'n' for not \n").lower()
      if another_card == 'y':
        user_cards.append(deal_card())
      else:
       the_game_over = True
  
  while computer_score != 0 and computer_score > 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f" You final hand is : {user_cards} and you score is : {user_score}")
  print(f" The hand of your opponent is {computer_cards}, final score : {computer_score}")
  print(compare(user_score, computer_score))

while input("You wanna play some black jack? Type 'y' or 'n' : \n") == 'y':
  the_game()
  