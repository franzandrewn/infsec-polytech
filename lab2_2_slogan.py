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

res = ''
for x in name:
	print(x, '=>', enc_str[alphabet.index(x)])
	res += enc_str[alphabet.index(x)]
print(res)