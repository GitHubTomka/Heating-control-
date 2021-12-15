import json


def change_hot_water():
  length = 2
  user_choice = ' '

  while len(user_choice) != length\
  or not user_choice.isdigit()\
  or user_choice < "35"\
  or user_choice > "85":
    user_choice = input("Podaj nową wartość (od 35 do 85 stopni): ")
  
    filename = 'change_temp.json' 
  with open(filename, 'r') as file:
    data = json.load(file)
    data['hot_water'] = user_choice
  with open(filename, 'w') as file:
    json.dump(data, file)
  print("Zmiana dodana pomyślnie!")


def change_heater_temp():
  length = 2
  user_choice = ' '

  while len(user_choice) != length\
  or not user_choice.isdigit()\
  or user_choice < "35"\
  or user_choice > "85":
    user_choice = input("Podaj nową wartość (od 35 do 85 stopni): ")
  
  filename = 'change_temp.json' 
  with open(filename, 'r') as file:
    data = json.load(file)
    data['heater'] = user_choice
  with open(filename, 'w') as file:
    json.dump(data, file)
  print("Zmiana dodana pomyślnie!")


def change_floor_temp():
  length = 2
  user_choice = ' '
  
  while len(user_choice) != length\
  or not user_choice.isdigit()\
  or user_choice < "25"\
  or user_choice > "50":
    user_choice = input("Podaj nową wartość (od 25 do 50 stopni): ")

  filename = 'change_temp.json' 
  with open(filename, 'r') as file:
    data = json.load(file)
    data['floor'] = user_choice
  with open(filename, 'w') as file:
    json.dump(data, file)
  print("Zmiana dodana pomyślnie!")
