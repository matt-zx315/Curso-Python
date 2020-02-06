from num2words import num2words


def numeros_para_caracteres(_menor=0, _maior=1000):
    total = ""

    for i in range(1, 1001):
        num = num2words(i, lang='pt-BR')
        total += num.replace(' ', '')

    return len(total)
