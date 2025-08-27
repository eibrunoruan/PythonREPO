# Desenvolva um programa que armazene quatro notas em uma lista e
# que apresente: a média final, a maior nota e a menor nota
notas = [10, 2, 2, 2]

def funcao(notas):
    if notas:

        media = sum(notas) / len(notas)
        maior = max(notas)
        menor = min(notas)

        return f'Media: {media}\nMaior nota: {maior}\nMenor nota: {menor}'
    return 'Sem notas'




# Desenvolva um programa que armazene quatro notas em uma lista e que apresente
# a média final. Caso a média seja igual ou superior a 7, apresentar a mensagem
# "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a
# média. Caso a nova média seja igual superior a 5, apresentar a mensagem
# "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"
def funcao2(notas):
    media = sum(notas) / len(notas)
    if notas:
        if media < 7:
            ultimanota = int(input('Insira a nota da Prova Final: '))
            notas.append(ultimanota)
            media = sum(notas) / len(notas)
            if media>= 5:
                return f'Aprovado'
            return f'Reprovado'
        return f'Aprovado'

if __name__ == '__main__':
    print(funcao(notas))
    print(funcao2(notas))