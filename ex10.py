# desenvolva um cod que leia ano de nascimento e o ano atual e calcule a idade, se for > 18 imprima "maior de idade", senao "menor de idade"

print("Bem Vindo - Acesso para maiores de 18 anos; informe os dados para começar! ")
num1= int(input("Digite o seu ano de nascimento: "))
num2 = 2026
#num2= int(input("Digite o ano atual: "))
total= num2 - num1
if total >= 18:
    print("Acesso Liberado - Você é maior de idade")
else:
    print("Acesso Negado - Você é menor de idade")

