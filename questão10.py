numsorteado = int(51)
tentativa = int(input("insira o seu número da sorte: "))

while numsorteado != tentativa:
    print("errou. você não está com sorte")
    tentativa = int(input("insira o seu número da sorte: "))

print("parabéns! Você acertou o número sorteado")