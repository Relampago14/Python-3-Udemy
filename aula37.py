# s1 = {1, 2, 3}
# s1.add(4)
# s1.discard(1)
#
#
# print(s1)
#
# for v in s1:
#     print(v)

# s1 = {1, 2, 3}
# s1.update([1, 2, 3, 4, 5], {5, 6, 7, 8})
#
# print(s1)

# l1 = [1, 2, 1, 2, 3, 4, 3, 4, 5, 6, 5, 6]
# l1 = set(l1)
# l1 = list(l1)
#
# print(l1)

# s1 = {1, 2, 3, 4, 5, 7}
# s2 = {1, 2, 3, 4, 5, 6}
# # s3 = s1 | s2
# # s4 = s1 & s2
# # s5 = s1 - s2
# s6 = s1 ^ s2
#
# print(s6)

# l1 = ['João', 'Marcos', 'Moreira']
# l2 = ['Marcos', 'Moreira', 'João', 'João', 'João', 'João', 'João', 'João', 'João']
#
# l1 = list(set(l1))
# l2 = list(set(l2))
#
# print(l1, l2)

l1 = ['João', 'Marcos', 'Moreira']
l2 = ['Marcos', 'Moreira', 'João', 'João', 'João', 'João', 'João', 'João', 'João']

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')
