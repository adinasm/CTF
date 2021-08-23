with open('chars.txt', 'r') as f:
	chars = f.read().rstrip().replace('Execute: ', ' ').split()
	flag = ''.join([chr(int(c)) for c in chars])

	print(flag)
	print(len(flag))
