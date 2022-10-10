#ler um numero e mostrar o dobro, triplo e raiz quadrada

n = int(input('Digite um numero para descobrir: '))
n2 = n*2
n3 = n*3
nr = n ** (1/2)

print('O Dobro de {} é igual a {}, o triplo é igual a {}, e sua raiz quadrada é {}'.format(n, n2, n3, nr))