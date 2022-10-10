#Faça um algoritmo que leia o salario de um funcionario e mostre seu reajuste com 15% de aumento

salario = float(input('Digite o valor do seu salario: '))
aumento = salario * 15 / 100
novosal = salario + aumento

print('Voce tera um aumento de: ', aumento)
print('Seu novo salario é no valor de', novosal)
