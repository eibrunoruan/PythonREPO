# Desenvolva um programa que tenha uma função que verifique se
# um número inteiro qualquer é par ou impar

def par_impar(num):
    if num % 2 == 0:
        return 'Par'
    return 'Impar'

print(par_impar(3))