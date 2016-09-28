def caught_speeding(speed, is_birthday):
  if (speed <= 60 and is_birthday == False) or (speed <= 65 and is_birthday == True):
    return 0
  elif (61 <= speed <= 80 and is_birthday == False) or (66 <= speed <= 85 and is_birthday == True):
    return 1
  else:
    return 2
  

