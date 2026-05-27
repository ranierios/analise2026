
# Calcula o imc combinando as entradas de peso e altura

# ajustando as casas decimais com f

print("Bem Vindo - Sou seu calculador de IMC ")
alt=float(input("digite a sua altura: "))
peso=float(input("digite o seu peso: " ))
imc= float(peso / (alt * alt)) 
print(f"Seu IMC é: {imc:.2f}")


# ajustando com Round

print("Bem Vindo - Sou seu calculador de IMC de novo ")
alt=float(input("digite a sua altura: "))
peso=float(input("digite o seu peso: " ))
imc = round(peso / (alt * alt), 2)
print("Seu IMC é:" , imc)







