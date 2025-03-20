from consts import alphabet, name

square = [[]]
for x in alphabet:
	last_len = len(square[len(square)-1])
	if last_len > 0 and last_len % 6 == 0:
		square.append([])
	square[len(square) - 1].append(x)
square[len(square) - 1].append(',')
square[len(square) - 1].append('.')
square[len(square) - 1].append('!')

print('Полибианский квадрат: ')
for x in square:
	print("\t".join(x))

res = ''
for ch in name:
	index = alphabet.index(ch)
	row = index // 6
	col = index % 6
	print(ch, '=>', square[row+1][col])
	res += square[row+1][col]
print(res)