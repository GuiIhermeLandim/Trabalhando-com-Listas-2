# Exercício 1
lista = []
listap = []
listai = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Deseja prosseguir? [S/N] ')).strip().upper()
    while r not in 'SN':
        print('Opção Inválida, tente novamente.')
        r = str(input('Deseja prosseguir? [S/N] ')).strip().upper()
    if r == 'N':
        print('Programa encerrado.')
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        listap.append(lista[c])
    else:
        listai.append(lista[c])
print(f'Lista completa: {lista}')
print(f'Lista de números Pares: {listap}')
print(f'Lista de números ímpares: {listai}')

# Exercício 2
dados = []
geral = []
pesos = []
cont = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    geral.append(dados[:])
    dados.clear()
    cont += 1
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        print('Por favor, selecione uma opção válida. ')
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if r == 'N':
        print('Programa encerrado. ')
        break
for p in geral:
    pesos.append(p[1])
pesos.sort()
print('=-'*30)
print(f'Total de pessoas Cadastradas: {cont}')
print(f'Cadastrados com o maior peso registrado ({pesos[-1]:.1f}Kg): ', end='')
for c in geral:
    if c[1] == pesos[-1]:
        print(f'[{c[0]}]', end=' ')
print(f'\nCadastrados com o menor peso registrado ({pesos[0]:.1f}Kg): ', end='')
for c in geral:
    if c[1] == pesos[0]:
        print(f'[{c[0]}]', end=' ')
