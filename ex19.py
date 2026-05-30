print("Bem Vindo a calculadora de Impostos!!")

var1= input("Digite o cargo desejado: ").lower()

if var1 == "caixa":
    salario_bruto = 1500
elif var1 == "vendedor":
    salario_bruto = 2400
elif var1 == "gerente":
    salario_bruto = 4000
else:
    salario_bruto = 0
    print("Você não trabalha aqui")

desconto_inss = salario_bruto * 0.12

if salario_bruto > 2000:
   desconto_irrf = salario_bruto * 0.14
else:
   desconto_irrf = salario_bruto * 0.08

salario_liq = salario_bruto - desconto_inss - desconto_irrf

print("----Demonstrativo de Pagamento-----")
print(f"Salario Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS: R$ {desconto_inss:.2f}")
print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
print(f"Salario Liquido: R$ {salario_liq:.2f}")


