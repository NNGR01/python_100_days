import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
run_again = True
the_final = []
the_diccionari = {}

def mayor_postor(the_diccionari):
  mas_alta = 0
  ganador = ""
  for n in the_diccionari:
    monto = the_diccionari[n]
    if monto > mas_alta:
      mas_alta = monto
      ganador = n
  print(f"thwe winner is {ganador} whit a bid of ${mas_alta}")    

while run_again:
  name = input('what´s your name\n ')
  bid = int(input('how much you bid\n '))
  the_diccionari[name] = bid
  ask = input('Other user want to bid?, type "yes" or "no"\n')  
  if ask == "yes":
    os.system('cls')
  elif ask == "no":
    run_again = False
    mayor_postor(the_diccionari)
    