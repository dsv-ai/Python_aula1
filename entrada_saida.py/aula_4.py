"""
Leia o preço de um produto e o percentual de desconto. Calcule e
exiba o valor final com desconto aplicado, com 2 casas decimais.

"""

print("Apenas Hoje!! Super desconto de 15 por cento na compra de qualquer produto da loja!!")


preco = float(input("Digite o Valor do seu produto escolhido? "))
desconto = (preco * 15 / 100) - 100 
print(f"Com o desconto de 15% o produto sai por apenas: {desconto:.2f}")# Consegui aplicar a lógica e com a função .2f consegui entrar o resultado esperado 






"""
preco = float(input("Digite o preço: "))
print(f"Preço: R$ {preco:.2f}")
"""