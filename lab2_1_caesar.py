from consts import alphabet, name

distance = 4

res = ''
for x in name:
	print(x, '=>', alphabet[alphabet.index(x) + distance])
	res += alphabet[alphabet.index(x) + distance]
print(res)