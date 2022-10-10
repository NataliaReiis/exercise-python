#Faça um programa que leia o preço de um produto e mostre seu novo preço comm 5% de desconto

preco = int(input('Qual o preço do produto? '))
desconto = preco * 5  / 100
novop = preco - desconto

print('O valor do produto é {}, e seu novo preço com desconto é {}'.format(preco, novop))