def combo_string(a,b):
	c = min(len(a),len(b))
	if len(a) == c:
		return a + b + a
	else:
		return b + a + b


