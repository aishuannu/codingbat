def last2(a):
	i = 0
	b = 0
	while i<len(a)-2:
		if a[i:i+2] == a[len(a)-2: ]:
			b = b+1 
			i += 1
		else:
			i += 1
 	return b


