def string_bits(a):
	b = ""
	i = 0
	while i<=len(a):
		b = b+a[i:i+1]
		i += 2
	return b

