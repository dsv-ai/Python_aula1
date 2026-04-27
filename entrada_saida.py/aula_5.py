"""
Leia o nome do aluno e 3 notas (float). Calcule a média e exiba um boletim 
formatado informando se foi aprovado (média ≥ 7.0) ou reprovado.

"""
print("Seja Bem vindo ao Boletim on-line! Digite seu nome e as suas três ultimas notas escolares:")
print("=" * 30)
nome = input("Digite seu nome: ")

n_1 = float(input("Digite sua primeira Nota: "))
n_2 = float(input("Digite sua segunda Nota: "))
n_3 = float(input("Digite sua Terceira Nota: "))

media = (n_1 + n_2 + n_3) // 3

if media >= 7.0:
    print("Estatus do Aluno (Aprovado!) ")

else:
    print("Estatus do Aluno (Reprovado!) ") # Nesse exercício resolvi usar a condição if e else para chegar o mais próximo do resltado esperado!



