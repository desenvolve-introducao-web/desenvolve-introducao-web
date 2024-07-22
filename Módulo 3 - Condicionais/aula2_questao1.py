print("Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade")
juliana = int(input("Insira a idade de Juliana: "))
cris = int(input("Insira a idade de Cris: "))
print("Juliana e Cris podem entrar no bar?", (juliana >= 18) and (cris >= 18))