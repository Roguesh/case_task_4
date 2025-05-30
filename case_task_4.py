from random import *

num = randint(1,100)

print("Программа загадала число от 1 до 100, попробуйте его угадать! У Вас 10 попыток.")

trycount = 10

while True:
  try:
    usr_num = int(input("Введите Ваше предположение в диапазоне от 1 до 100: "))
    if usr_num == 0 or usr_num > 100:
      print(usr_num, " не является числом в диапазоне от 1 до 100!")
    elif usr_num < num:
      trycount -= 1
      print("Ваше число меньше загаданного. \nУ вас осталось: ", trycount, "попыток.")
      if trycount == 0:
        print("Вы потратили все попытки, Вы проиграли!")
        break
    elif usr_num > num:
      trycount -= 1
      print("Ваше число больше загаданного. \nУ вас осталось: ", trycount, "попыток.")
      if trycount == 0:
        print("Вы потратили все попытки, Вы проиграли!")
        break
    else:
      result = 10 - trycount
      if result == 1:
        print("Поздравляем! Вы угадали загаданное число с ", result, "попытки!")
        break
      elif result == 2 or result == 3:
        print("Поздравляем! Вы угадали загаданное число за ", result, "попытки!")
        break
      else:
        print("Поздравляем! Вы угадали загаданное число за ", result, "попыток!")
        break
  except ValueError:
    print("Вы ввели не число!")