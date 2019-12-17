"""
Utilizado para sair de loops de maneira projetada.
"""

for num in range(0, 10):
    if num == 5:
        break
    else:
        print(num)

print("Fora do loop.")

while True:
    comando = input("Digite \"Sair\" para encerrar. ").lower()

    if comando == "sair":
        break