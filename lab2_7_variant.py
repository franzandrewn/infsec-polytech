from consts import alphabet, name, matrix_find
import random

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
	last_len = len(square[len(square) - 1])
	if last_len > 0 and last_len % 6 == 0:
		square.append([])
	square[len(square) - 1].append(x)
square[len(square) - 1].append(',')
square[len(square) - 1].append('.')
square[len(square) - 1].append('!')

for x in square:
	print("\t" + "\t".join(x))

# print(matrix_find(square, 'Я'))
row_encodings = ['ФЫ', 'ВА', 'ПР', 'ОЛ', 'ДЖ', 'ЭЯ']
col_encodings = ['ЙЦ', 'УК', 'ЕН', 'ГШ', 'ЩЗ', 'ХЪ']
print("\t".join(row_encodings))
print("\t".join(col_encodings))
res = ''
for i in name:
	x, y = matrix_find(square, i)
	res += random.choice(row_encodings[x])
	res += random.choice(col_encodings[y])
	print(i, '=>', res[-2:])

print(res)
