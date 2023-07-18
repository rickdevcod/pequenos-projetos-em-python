

#funcão,calculo do fatorial com indice, utilizei como parametro para a função "num"
def fatorial(num):
    resultado = 1
    for  i in range(1, num + 1):
        resultado *= i
    return resultado

# a concatenação
minutos = int(input("Digite os minutos atuais:"))
fatorial_minutos = fatorial(minutos)
senha = "LIBERDADE" + str(fatorial_minutos)
print(" A senha para desbloqueio:", senha)

#adicionando a chamada do programa, caso o professor abra pelo prompt
input("Pressione para sair ... ")