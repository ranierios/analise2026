# Codigo que leia uma idade e seguindo a logica real da vida imprima se é menor, maior de idade ou idoso


idade = int(input("digite sua idade: "))
if idade < 18 :
    print("Menor de idade")
#elif idade >= 18 and idade <= 60 :
#    print ("Maior de Idade")
 
elif idade >= 60 :
    print ("Idoso")
else :
    print("Maior de idade")



