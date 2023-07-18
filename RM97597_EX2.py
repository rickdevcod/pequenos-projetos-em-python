def laco_mais_inicio_programa():
    continuar = True
    while continuar:
        print("rdevcod")
        print("**********************************************")
        print("Bem vindo, informe a quantidade de votos abaixo!")
        print("**********************************************")
        try:
            # variaveis prontas para receber numeros inteiros int(input))
            segunda = int(input("Informe a quantidade de votos para Segunda-feira:"))
            terca = int(input("Informe a quantidade de votos para Terca-feira:"))
            quarta = int(input("Informe a quantidade de votos para Quarta-feira:"))
            quinta = int(input("Informe a quantidade de votos para Quinta-feira:"))
            sexta = int(input("Informe a quantidade de votos para Sexta-feira:"))
        except ValueError:
            print("Entrada inválida. Informe um número inteiro.")
            continue

        def logica_do_programa():
            # logica do programa, se segunda for maior que terça e segunda for maior que quarta e segunda for maior que quinta e ...
            if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
                print("Segunda-feira obteve mais votos")
            elif terca > quarta and terca > quinta and terca > sexta:
                print("Terça-feira obteve mais votos")
            elif quarta > quinta and quarta > sexta:
                print("Quarta-feira obteve mais votos")
            elif quinta > sexta:
                print("Quinta-feira obteve mais votos")
            # a sexta feira é o unico dia que por ser o ultimo dia ele não é maior que ninguém, então ele cai no else.
            else:
                print("Sexta-feira obteve mais votos")

        logica_do_programa()

        #opcao e a variavel de entrada para perguntar ao usuario se ele quer tentar novamente.
        #abaixo a logica, se variavel opcao.upper upper a pessoa pode digitar maiusculo ou minusculo, for igual igual a "N"
        #continuar se torna falso e então o programa para, se a pessoa digitar S ele cai no continuar no inicio do programa.
        opcao = input("Deseja tentar novamente? (S/N)")
        if opcao.upper() == "N":
            print("Fim")
            continuar = False

#Chamada da função para iniciar o programa e fazer o laço, o chamado da função main pra funcionar deve ser chamado ao fim do programa.
laco_mais_inicio_programa()
