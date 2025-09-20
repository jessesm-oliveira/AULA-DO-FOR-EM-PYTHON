
for c in range(1,10): # C é uma variavel contador, ele serva para contar quantas vezes oi será mostrado
    print('oi')
print('fim')

print(100*('*'))


for c in range(1,10) : # C é uma variavel contador, ele serva para contar quantas vezes oi será mostrado
    print(c)
print('fim')

print(100*('*'))

for c in range(10,0,-1): # CONTAGEM REGRESSIVA, COMEÇA EM 10, VAI ATÉ 0, E O -1 É PARA DIMINUIR DE 1 EM 1
    print(c) # MOSTRANDO O VALOR DE C
print('fim')


print(100*('*'))


num=int(input('digite um número')) # VARIAVEL NUM PARA GUARDAR O NÚMERO QUE O USUÁRIO DIGITAR

for c in range(0,num): # REPETIÇÃO DE 0 ATÉ O NÚMERO QUE O USUÁRIO DIGITAR
    print(c)


print(100*('*'))


i= int(input('digite o inicio :')) # VARIAVEL I PARA INICIO 

f=int(input('digite o fim :')) # VARIAVEL F PARA O FIM

p=int(input('digite o passo:')) # VARIAVEL P PARA PASSOS  E QUANTOS VAI PULANDO 

for c in range(i,f+1,p): # REPETIÇÃO DE I ATÉ F, PULANDO DE P EM P
    print(c)



print(150*('*')) # MOSTRANDO 150 VEZES O CARACTERE


soma=0 # VARIAVEL SOMA PARA GUARDAR A SOMA DOS VALORES
for c in range(1,4): # REPETIÇÃO DE 3 VEZES
    n=int(input('digite o valor ---> ')) # VARIAVEL N PARA GUARDAR O VALOR QUE O USUÁRIO DIGITAR
    soma += n # SOMA O VALOR DE N NA VARIAVEL SOMA
print(f" A SOMATÓRIA FOI DE ------> {soma}") # MOSTRA O VALOR DA SOMA