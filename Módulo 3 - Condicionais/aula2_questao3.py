idade = int(input("Digite sua idade: "))
quantidade = int(input("Já jogou quantos jogos de tabuleiro? "))
vitorias = int(input("Quantos jogos já venceu? "))
print("Aptidão para ingressar no clube de jogos de tabuleiro: ", (idade < 19 or idade > 15) and (quantidade >= 3) and (vitorias > 0))