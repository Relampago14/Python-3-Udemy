"""texto = 'João'

c = 0

while c < len(texto):
    print(texto[c])
    c += 1

print()
print('Fim')
"""

"""texto = 'João'

for l in texto:
    print(l)

print()
print('Fim')"""

"""for n in range(10, -1, -1):
    print(n)

print('Fim')"""
"""
for n in range(81):
    if n % 8 == 0:
        print(n)
"""

texto = 'João Marcos'
nova_str = ''

for l in texto:
    if l == 'o':
        nova_str = nova_str + l.upper()
    elif l in 'aeiou':
        break
    else:
        nova_str += l


print(nova_str)
