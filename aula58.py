def lista_clientes(clientes, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes)
    return lista


lista_clientes1 = ['Fabrício']
clientes1 = lista_clientes(['João', 'Maria', 'Eduardo'], lista_clientes1)
clientes2 = lista_clientes(['Marcos', 'Jonatas', 'Romário'])
clientes3 = lista_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
