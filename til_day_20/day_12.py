import random

print("""
         _____                          _    _             _   _                    _                 
  / ____|                        | |  | |           | \ | |                  | |                
 | |  __  _   _   ___  ___  ___  | |_ | |__    ___  |  \| | _   _  _ __ ___  | |__    ___  _ __ 
 | | |_ || | | | / _ \/ __|/ __| | __|| '_ \  / _ \ | . ` || | | || '_ ` _ \ | '_ \  / _ \| '__|
 | |__| || |_| ||  __/\__ \\__ \ | |_ | | | ||  __/ | |\  || |_| || | | | | || |_) ||  __/| |   
  \_____| \__,_| \___||___/|___/  \__||_| |_| \___| |_| \_| \__,_||_| |_| |_||_.__/  \___||_|  
     """)

print("I'm think in a number between 1 to 100")

random_number = random.randint(1, 100)

end = True

counts = 10

def compare():
  global end
  global counts
  input_number = int(input(f"what number I'm thinking? : "))
  if input_number > random_number:
    print(f"Too high, you have {counts} attempts left")
  elif input_number < random_number:
    print(f"Too low, you have {counts} attempts left")
  else:
    print(f"You win, the answer was {random_number}")
    end = False
  
level = input("choose the level 'hard' or 'easy' : ").lower() 

if level == 'hard':
  counts = 5
  
while end:
  counts -= 1
  compare()
  if counts == 0:
    end = False
    print("you lose")