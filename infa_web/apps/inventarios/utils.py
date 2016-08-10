
def sum_invini(value):
	value_sum = str(int(value[3:])+1)
	cant_space = 5-int(len(value_sum))
	return 'II-'+(cant_space*'0')+value_sum