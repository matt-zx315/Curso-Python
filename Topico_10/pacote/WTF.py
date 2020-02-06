def palindromo(_max=1000):
    maior_palindromo = 0

    for x in range(0, _max):
        for y in range(0, _max):
            numero = x * y
            string = str(numero)
            print(x, y, numero)
            tamanho = len(string)
            confirma_palindromo = True

            for i in range(len(string) // 2):
                if string[i] == string[tamanho - (i + 1)]:
                    confirma_palindromo = True
                else:
                    confirma_palindromo = False
                    break

            if confirma_palindromo:
                maior_palindromo = numero

    return maior_palindromo
