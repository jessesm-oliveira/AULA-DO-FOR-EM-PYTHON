# FAÇA UM PROGRAMA QUE PERGUNTE QUAL TABUADA O USUÁRIO QUER IMPRIMIR.

import os # IMPORTANDO A BIBLIOTECA OS PARA USAR A FUNÇÃO SYSTEM
import time # IMPORTANDO A BIBLIOTECA OS PARA USAR A FUNÇÃO SYSTEM
os.system('cls') # FUNÇÃO SYSTEM PARA LIMPAR A TELA TERMINAL

num = int(input('Digite um número para ver sua tabuada: ')) # VARIAVEL NUM PARA GUARDAR O NÚMERO QUE O USUÁRIO DIGITAR

for c in range(0, 11): # REPETIÇÃO DE 0 ATÉ 10
    time.sleep(1) # FUNÇÃO SLEEP PARA DAR UMA PAUSA DE 1 SEGUNDO
    print(f'~~~~~~~~~~ > {num} x {c} = {num*c} <~~~~~~~~~~') # MOSTRANDO A TABUADA

print('~~~~~~~~~~ FIM DA TABUADA, OBRIGADO POR USAR MEU PROGRAMA!!! ~~~~~~~~~~') # MENSAGEM DE FIM DA TABUADA