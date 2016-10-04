def xyz_there(str):
  for i in range(-1, len(str)):
    if str[i + 1 : i + 4] == "xyz" and str[i] != ".":
      return True
      break
  return False

