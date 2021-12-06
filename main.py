import change_temp
import sys


def menu_cwu():
  dlugosc = 1
  wybor_uzytkowanika = " "

  while len(wybor_uzytkowanika) != dlugosc or not wybor_uzytkowanika.isdigit():
    print("\nMenu CWU")
    filename = 'change_temp.txt' 
    with open(filename, 'r') as f:
      output = f.read()
    print(f"Temperatura nastawiona - {output}") 
    print("Temperatura w zbiorniku - 55")
    print("1 - Zmień temperaturę")
    print("2 - Powrót")
    wybor_uzytkowanika = input("\nWybierz: ")
    if wybor_uzytkowanika == "1":
      change_temp.menu_cwu_zm_temp()
      menu_cwu()
    if wybor_uzytkowanika == "2":
      menu_sterownika()
    if wybor_uzytkowanika >= "3":
      menu_cwu()


def menu_grzejnikowe():
  dlugosc = 1
  wybor_uzytkowanika = " "

  while len(wybor_uzytkowanika) != dlugosc or not wybor_uzytkowanika.isdigit():
    print("\nMenu Ogrzewania grzejnikowego")
    filename = 'change_temp2.txt' 
    with open(filename, 'r') as f:
      output = f.read()
    print(f"Temperatura nastawiona - {output}") 
    print("Temperatura zaworu - 51")
    print("1 - Zmień temperaturę")
    print("2 - Powrót")
    wybor_uzytkowanika = input("\nWybierz: ")
    if wybor_uzytkowanika == "1":
      change_temp.menu_grzejnik_zm_temp()
      menu_grzejnikowe()
    if wybor_uzytkowanika == "2":
      menu_sterownika()
    if wybor_uzytkowanika >= "3":
      menu_grzejnikowe()


def menu_podlogowe():
  dlugosc = 1
  wybor_uzytkowanika = " "

  while len(wybor_uzytkowanika) != dlugosc or not wybor_uzytkowanika.isdigit():
    print("\nMenu Ogrzewania podłogowego")
    filename = 'change_temp3.txt' 
    with open(filename, 'r') as f:
      output = f.read()
    print(f"Temperatura nastawiona - {output}") 
    print("Temperatura zaworu - 30")
    print("1 - Zmień temperaturę")
    print("2 - Powrót")
    wybor_uzytkowanika = input("\nWybierz: ")
    if wybor_uzytkowanika == "1":
      change_temp.menu_podlogowe_zm_temp()
      menu_podlogowe()
    if wybor_uzytkowanika == "2":
      menu_sterownika()
    if wybor_uzytkowanika >= "3":
      menu_podlogowe()


def menu_sterownika():
  dlugosc = 1
  wybor_uzytkowanika = " "

  while len(wybor_uzytkowanika) != dlugosc or not wybor_uzytkowanika.isdigit():
    print("\n---Menu główne---")
    print("0 - CWU")
    print("1 - Ogrzewanie grzejniowe")
    print("2 - Ogrzewanie podłogowe")
    print("3 - Wyjście")
    wybor_uzytkowanika = input("\nWybierz: ")

  if wybor_uzytkowanika == "0":
    menu_cwu()

  if wybor_uzytkowanika == "1":
    menu_grzejnikowe()

  if wybor_uzytkowanika == "2":
    menu_podlogowe()
  
  if wybor_uzytkowanika == "3":
    sys.exit()

  if wybor_uzytkowanika >="4":
    menu_sterownika()
  
menu_sterownika()