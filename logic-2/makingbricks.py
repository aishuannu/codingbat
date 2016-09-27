def make_bricks(small, big, goal):
  if goal/5 <= big and goal%5 <= small:
    return True
  elif big >0 and 0 <= goal - (5*big) <= small:
    return True
  elif big == 0 and goal <= small:
    return True
  else:
    return False
    
