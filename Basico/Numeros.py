# Números
# Desenvolva um programa que leia um número inteiro qualquer e que apresete
# o número informado, seguido do seu antecessor e do seu sucessor
def antecessor_sucessor():
    number = int(input('---- Antecessor e Sucesso ----\nDigite um número:'))
    return f'Seu numero é {number} e seu sucessor/antecessor são: {number +1 } e {number - 1} '

# Desenvolva um programa que leia um número inteiro qualquer e que apresente
# o número informado com duas casas decimais2
def duas_casas():
    number = int(input('Digite um número: '))
    return f'Sua numero com duas casas: {number: 0.2f} '

# Desenvolva um programa que leia quatro notas e que apresente a média final
def media():
    notas = []
    cout = 0
    for cout in range(4):
        notas.append(float(input('Digite sua nota: ')))
        cout += 1
    return sum(notas) / cout


# Desenvolva um programa que leia um número inteiro qualquer e que informe se
# este número é par ou impar
def par_impar():
    num = int(input('Digite um Numero'))
    if num % 2 == 0:
        return 'Par'
    return 'Impar'

if __name__ == '__main__':
    print(antecessor_sucessor())
    print(duas_casas())
    print(media())
    print(par_impar())