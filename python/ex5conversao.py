#escrever um algoritmo que leia um numero em mentro e o exiba em centimentro e milimetro

n = int(input('Digite um numero para ver sua conversão'))
ncm = n * 100
nmm = n * 1000

print('{} metros é igual a {}cm e {}mm'.format(n, ncm, nmm))