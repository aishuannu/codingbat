def double_char(str):
  newstr = str[0] * 2
  for i in range(1, len(str)):
    newstr = newstr + str[i] * 2
  return newstr

