def sum(a, b):
	return a + b

def sum_many(*args):
	sum = 0
	for i in args:
		sum = sum + i
	return sum

def sum_mul(choice, *args):
	if choice == 'sum':
		result = 0
		for i in args:
			result = result + i
	elif choice == 'mul':
		result = 1
		for i in args:
			result = result * i
	
	return result

a = 1
def vartest():
	global a
	a = a + 1

vartest()
print(a)