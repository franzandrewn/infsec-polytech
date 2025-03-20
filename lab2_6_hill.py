import numpy
from consts import alphabet, name

while len(name) % 3 != 0:
    name += 'Я'
print(name)

triples = []
while len(name) > 0:
    first = alphabet.index(name[0])
    second = alphabet.index(name[1])
    third = alphabet.index(name[2])
    triple = [[first],[second],[third]]
    triples.append(numpy.array(triple, dtype=int))
    name = name[3:]

for triple in triples:
    print(triple)

encoding_matrix = numpy.array([[6, 27, 1], [13, 16, 32], [28, 17, 15]])
print(encoding_matrix)

res_triples = []
for triple in triples:
    temp = numpy.dot(encoding_matrix, triple)
    temp[0][0] = temp[0][0] % 33
    temp[1][0] = temp[1][0] % 33
    temp[2][0] = temp[2][0] % 33
    print(temp)
    res_triple = alphabet[temp[0][0]] + alphabet[temp[1][0]] + alphabet[temp[2][0]]
    res_triples.append(res_triple)
print(res_triples)
print("".join(res_triples))
