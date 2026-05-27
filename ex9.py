# desenvolva um codigo que calcula 2 valores e calcule a media. Se a media for maior q 5 imprima aprovado, senao imprima recuperação;

print("Bem Vindo - Seu Boletim Online! ")
a=float(input("digite a sua nota da primeira prova: "))
b=float(input("digite a sua nota da segunda prova: "))
resultado= float((a+b)/(2))
#print(resultado)
if resultado > 5:
    print (f"Situação: Aprovado com média {resultado}")
else:
    print (f"Situação: Recuperação com média {resultado}")



