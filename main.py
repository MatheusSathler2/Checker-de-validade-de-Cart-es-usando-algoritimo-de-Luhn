working = True
while working:
    while True:
        try:
            X = int(input("Digite o numero do seu Cartao para verificar se ele e valido: [escreva somente numeros, sem espacamento]:  " ))
            break
        except ValueError:
            print('Digite apenas numeros: ')
    X2 = str(X)
    X3 = []
    X4 = []
    X5 = []
    for letra in X2:
        letra2 = int(letra)
        X3.append(letra2)
    if len(X3) != 16:
        print("Verifique se o numero do cartao foi digitado corretamente")
    elif len(X3) == 16:
        for i in X3:
            if i % 2 == 0:
                Intervalo = X3[i] * 2
                if Intervalo > 9:
                    Intervalo = Intervalo - 9
                    X4.append(Intervalo)
            else:
                Intervalo2 = X3[i]
                X5.append(Intervalo2)
        soma = sum(X4) + sum(X5)
        if soma % 10 == 0:
            print("Seu cartao e valido")
        else:
            print("Seu cartao nao e valido")
    while True:
        pergunta = input("Deseja inserir outro cartao? S/N: ").strip().upper()
        if pergunta == ("N"):
            working = False
            break
        elif pergunta == ("S"):
            working = True
            break
        else:
            print("Por favor, digite S para Sim e N para Nao")
            continue

