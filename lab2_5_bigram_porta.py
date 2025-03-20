from consts import alphabet, name

modded_alphabet = alphabet
modded_alphabet.remove('Й')
modded_alphabet.remove('Ё')
print(modded_alphabet)

res = ''
for i in range(0, len(name), 2):
	x = modded_alphabet.index(name[i])
	y = modded_alphabet.index(name[i+1])
	print(name[i] + name[i + 1],
		  x + 1, 'строка,',
		  y + 1, 'столбец,',
		  'код =', x*31+y+1)
	res += str(x*31+y+1) + ' '

print(res)
