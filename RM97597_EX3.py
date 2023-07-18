
#Parte 1: criar a lista vazia
lista_notas = []
print("Bem vindo ao Programa de soma de média por turmas Par e Ímpar:.\n O programa pede para digitar as notas em sequencias:.\n ÍMPAR E PAR: Veja abaixo")
def recebendo_notas():
    for i in range(1, 21):
        if i % 2 != 0:
            print(f"Você está digitando as notas dos alunos ÍMPARES.\nPor favor, insira a nota do aluno de número {i}:")
        else:
            print(f"Você está digitando as notas dos alunos PARES.\nPor favor, insira a nota do aluno de número  {i}:")
        nota = float(input())
        lista_notas.append(nota)
recebendo_notas()
#Parte 3: calcular a média de cada turma
def calculando_media():
    media_impares = 0
    media_pares = 0
    for i in range(len(lista_notas)):
        if i % 2 != 0:
            media_impares += lista_notas[i]
        else:
            media_pares += lista_notas[i]

    media_impares /= 10
    media_pares /= 10
    return media_impares, media_pares

media_impares, media_pares = calculando_media()

def exibir_msg_media():
    if media_impares > media_pares:
        maior_media = "ímpares"
    else:
        maior_media = "pares"

    print(f"A média da turma dos alunos ímpares é {round(media_impares, 2)}.\nA média da turma dos alunos pares é {round(media_pares, 2)}.\nA turma com a maior média é a dos alunos {maior_media}.")

exibir_msg_media()














