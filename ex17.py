# desenvolva um cód que verifique se a temperatura esta frio, agradavel ou calor
# siga tabela abaixo
# < 18 frio
#entre 18 e 30 = agradavel
# > 30 = calor

temp= float(input("Digite a temperatura desejada: "))
if temp < 18 :
    print(f" Frio - Temperatua setada em {temp}")
elif temp >= 18 and temp < 30 :
    print(f" Agradavel - Temperatura setada em {temp}")
else :
    print(f" Calor - Temperatura setada em {temp}")

