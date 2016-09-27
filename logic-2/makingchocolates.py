def make_chocolate(small, big, goal):
  if goal/5 <= big and goal%5 <= small:
    return goal%5
  elif big >0 and 0 <= goal - (5*big) <= small:
    return goal - (5*big)
  elif big == 0 and goal <= small:
    return goal
  else:
    return -1
    

