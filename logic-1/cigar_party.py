def cigar_party(cigars, is_weekend):
  if (40 <= cigars <= 60 and is_weekend == False) or (cigars >= 40 and is_weekend == True):
    return True
  else:
    return False

