from consts import alphabet, name, matrix_find

slogan_zero = 'АНДРЕЙ'
slogan = ''
print("Изначальный слоган: ", slogan_zero)

for x in slogan_zero:
	if x not in slogan:
		slogan += x
print("Слоган без повторений:", slogan)
slogan = slogan.ljust(10, ' ')

square = [list([x for x in slogan])]
for x in alphabet:
	if x not in square[0]:
		last_len = len(square[len(square) - 1])
		if last_len > 0 and last_len % 10 == 0:
			square.append([])
		square[len(square) - 1].append(x)
while len(square[len(square) - 1]) < 10:
	square[len(square) - 1].append(' ')

for x in square:
	print("\t".join(x))

col_encodings = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

res = ''
for i in name:
	x, y = matrix_find(square, i)
	temp = str(x) if x != 0 else ''
	temp += str(col_encodings[y])
	res += temp
	print(i, '=>', temp)

print(res)