reais = float(input("Insira o valor em real brasileiro para calcularmos o número mínimo de notas para alcançá-lo: "))
c100 = int(reais // 100)
reais %= 100
c50 = int(reais // 50)
reais %= 50
c20 = int(reais // 20)
reais %= 20
c10 = int(reais // 10)
reais %= 10
c5 = int(reais // 5)
reais %= 5
c2 = int(reais // 2)
reais %= 2
c1 = int(reais // 1)
print(f"{c100} nota(s) de R$100,00")
print(f"{c50} nota(s) de R$50,00")
print(f"{c20} nota(s) de R$20,00")
print(f"{c10} nota(s) de R$10,00")
print(f"{c5} nota(s) de R$5,00")
print(f"{c2} nota(s) de R$2,00")
print(f"{c1} nota(s) de R$1,00")