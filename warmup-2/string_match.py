def string_match(a,b):
	i = 0
	c = 0
	while i <= min(len(a),len(b)) - 2:
		if a[i:i+2] == b[i:i+2]:
			c = c+1
			i += 1
		else:
			i +=1
	return c

