#Faça um programa que leia a largura e altura de uma parede em metros, calcule sua area e a quantidade
#de tinta necessaria para pinta-la, sabendo que cade l de tinta pinta 2 m.

h = int(input('Digite a altura da parede: '))
l = int(input('Digite agora a largura da parede: '))
a = l * h
tinta = a / 2

print('Sua area total é de {}, voce precisa de {} litros de tinta para pintar toda a parede :)'.format(a, tinta))