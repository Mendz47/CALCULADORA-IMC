print('\033[1;32m-=\033[m' * 8)
print('\033[1;36mCALCULADORA IMC\033[m')
print('\033[1;32m-=\033[m' * 8)
peso = float(input('\033[32mDigite o seu peso:\033[m '))
altura = float(input('\033[32mDigite a sua altura:\033[m '))
imc = peso / altura ** 2
if imc <= 18.5:
    print('\033[36mO seu IMC é\033[m \033[32m{:.2f}\033[m \033[36me você está ABAIXO do peso.\033[m'.format(imc))
elif imc <= 25:
    print('\033[32mO seu IMC é\033[m \033[32m{:.2f}\033[m \033[32me vocÊ está no peso IDEAL.\033[m'.format(imc))
elif imc <= 30:
    print('\033[33mO seu IMC é\033[m \033[32m{:.2f}\033[m \033[32me vocÊ está SOBREPESO.\033[m'.format(imc))
elif imc <= 40:
    print('\033[31mO seu IMC é\033[m \033[32m{:.2f}\033[m \033[31me você está OBESO.\033[m'.format(imc))
else:
    print('\033[35mO seu IMC é\033[m \033[32m{:.2f}\033[m \033[35me você está com OBESIDADE MÓRBIDA\033[m.'.format(imc))
