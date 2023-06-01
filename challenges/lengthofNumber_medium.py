def number_length(num):
	l = 1
	while num >= 10:
		num = num/10
		l = l +1
	return l