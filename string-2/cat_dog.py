def cat_dog(str):
  count = 0
  count1 = 0
  for i in range(len(str)):
    if str[i : i + 3] == "cat":
      count = count + 1
    elif str[i : i + 3] == "dog":
      count1 = count1 + 1
  if count == count1:
    return True
  else:
    return False

