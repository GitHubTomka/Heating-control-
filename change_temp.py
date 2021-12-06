def menu_cwu_zm_temp():
  dlugosc = 2
  wybor_uzytkowanika = ' '
  while len(wybor_uzytkowanika) != dlugosc\
  or not wybor_uzytkowanika.isdigit()\
  or wybor_uzytkowanika < "35"\
  or wybor_uzytkowanika > "85":
    wybor_uzytkowanika = input("Podaj nową wartość (od 35 do 85 stopni): ")
    filename = 'change_temp.txt' 
  with open(filename, 'w') as file:
    file.write(f"{wybor_uzytkowanika}")
  print("Zmiana dodana pomyślnie!")

def menu_grzejnik_zm_temp():
  dlugosc = 2
  wybor_uzytkowanika = ' '
  while len(wybor_uzytkowanika) != dlugosc\
  or not wybor_uzytkowanika.isdigit()\
  or wybor_uzytkowanika < "35"\
  or wybor_uzytkowanika > "85":
    wybor_uzytkowanika = input("Podaj nową wartość (od 35 do 85 stopni): ")
  filename = 'change_temp2.txt' 
  with open(filename, 'w') as file:
    file.write(f"{wybor_uzytkowanika}")
  print("Zmiana dodana pomyślnie!")

def menu_podlogowe_zm_temp():
  dlugosc = 2
  wybor_uzytkowanika = ' '
  while len(wybor_uzytkowanika) != dlugosc\
  or not wybor_uzytkowanika.isdigit()\
  or wybor_uzytkowanika < "25"\
  or wybor_uzytkowanika > "50":
    wybor_uzytkowanika = input("Podaj nową wartość (od 25 do 50 stopni): ")
  filename = 'change_temp3.txt' 
  with open(filename, 'w') as file:
    file.write(f"{wybor_uzytkowanika}")
  print("Zmiana dodana pomyślnie!")
