def not_string(a):
    b = len(a) - 1
    if b < 2:
	return "not" + a
    elif a[0] + a[1] + a[2] == "not":
	return a
    else:
	return "not" + a
    
