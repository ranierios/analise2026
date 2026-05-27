
# calcula uma porcentagem sobre valores
p=float(input("Digite o valor a ser acrescentado 10%: "))
r= (p * 0.1) + p
print("O valor a pagar é ", r)



# calcula uma porcentagem sobre produto e apresenta o valor final
produto = float(input("Digite o valor do produto (R$): "))
desconto = float(input("Digite o (%) de desconto desejado: "))
valor_desconto = produto * (desconto / 100)
valor_final = produto - valor_desconto
print(f"O valor com desconto é: {valor_final}")









