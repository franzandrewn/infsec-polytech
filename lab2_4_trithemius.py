from consts import alphabet, name

slogan_zero = 'АНДРЕЙГЕННАДЬЕВИЧ'
slogan = ''
print("Изначальный слоган: ", slogan_zero)

for x in slogan_zero:
	if x not in slogan:
		slogan += x
print("Слоган без повторений:", slogan)

enc_str = slogan
for x in alphabet:
	if x not in enc_str:
		enc_str += x
print('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
print("Строка для шифрования: ", enc_str)

square = [[]]
for x in enc_str:
	last_len = len(square[len(square)-1])
	if last_len > 0 and last_len % 6 == 0:
		square.append([])
	square[len(square) - 1].append(x)
square[len(square) - 1].append(',')
square[len(square) - 1].append('.')
square[len(square) - 1].append('!')

print('Таблица Трисемуса: ')
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