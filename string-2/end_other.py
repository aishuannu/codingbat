def end_other(a, b):
  a = a.lower()
  b = b.lower()
  c = min(len(a), len(b))
  if len(a) == c:
    for i in range(len(b)):
      if b[i : ] == a:
        return True
  else:
    for i in range(len(a)):
      if a[i : ] == b:
        return True
  return False
