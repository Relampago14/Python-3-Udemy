# from itertools import combinations
#
# pessoas = ['João', 'Marcos', 'Moreira']
#
# for g in combinations(pessoas, 2):
#     print(g)

# from itertools import permutations
#
# pessoas = ['João', 'Marcos', 'Moreira']
#
# for g in permutations(pessoas, 2):
#     print(g)

from itertools import product

pessoas = ['João', 'Marcos', 'Moreira']

for g in product(pessoas, repeat=2):
    print(g)
    