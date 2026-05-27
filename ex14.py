# crie um sistema de alistamento militar onde apenas está apto para o alistamento pessoas 18 anos ou mais e do sexo masculino

print("Bem Vindo ao Portal de Alistamento Militar")
gen = input("Digite o seu genero (M-masculino ou F-feminino): ").upper()
num1= int(input("Digite o seu ano de nascimento: "))
num2= 2026
total= num2 - num1
if total >= 18 and gen == "M" :
    print("Você está apto para o alistamento")
else :
    print ("Você não é apto para o alistamento")
print("teste")
print("teste 2")

