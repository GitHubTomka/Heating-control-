import change_temp
import sys
import json


def menu_hot_water():
  length = 1
  user_choice = " "

  while len(user_choice) != length or not user_choice.isdigit():
    print("\nMenu CWU")
    filename = 'change_temp.json' 
    with open(filename, 'r') as f:
      output = json.load(f)
    print(f"Temperatura nastawiona - {output['hot_water']}")
    print("Temperatura w zbiorniku - 55")
    print("1 - Zmień temperaturę")
    print("2 - Powrót")
    user_choice = input("\nWybierz: ")
    if user_choice == "1":
      change_temp.change_hot_water()
      menu_hot_water()
    if user_choice == "2":
      menu_controller()
    if user_choice >= "3":
      menu_hot_water()


def menu_heater():
  length = 1
  user_choice = " "

  while len(user_choice) != length or not user_choice.isdigit():
    print("\nMenu Ogrzewania grzejnikowego")
    filename = 'change_temp.json' 
    with open(filename, 'r') as f:
      output = json.load(f)
    print(f"Temperatura nastawiona - {output['heater']}") 
    print("Temperatura zaworu - 51")
    print("1 - Zmień temperaturę")
    print("2 - Powrót")
    user_choice = input("\nWybierz: ")
    if user_choice == "1":
      change_temp.change_heater_temp()
      menu_heater()
    if user_choice == "2":
      menu_controller()
    if user_choice >= "3":
      menu_heater()


def menu_floor():
  length = 1
  user_choice = " "

  while len(user_choice) != length or not user_choice.isdigit():
    print("\nMenu Ogrzewania podłogowego")
    filename = 'change_temp.json' 
    with open(filename, 'r') as f:
      output = json.load(f)
    print(f"Temperatura nastawiona - {output['floor']}") 
    print("Temperatura zaworu - 30")
    print("1 - Zmień temperaturę")
    print("2 - Powrót")
    user_choice = input("\nWybierz: ")
    if user_choice == "1":
      change_temp.change_floor_temp()
      menu_floor()
    if user_choice == "2":
      menu_controller()
    if user_choice >= "3":
      menu_floor()


def menu_controller():
  length = 1
  user_choice = " "

  while len(user_choice) != length or not user_choice.isdigit():
    print("\n---Menu główne---")
    print("0 - CWU")
    print("1 - Ogrzewanie grzejniowe")
    print("2 - Ogrzewanie podłogowe")
    print("3 - Wyjście")
    user_choice = input("\nWybierz: ")

  if user_choice == "0":
    menu_hot_water()

  if user_choice == "1":
    menu_heater()

  if user_choice == "2":
    menu_floor()
  
  if user_choice == "3":
    sys.exit()

  if user_choice >="4":
    menu_controller()
  
menu_controller()