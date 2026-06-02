#Desenvolva um codigo em phyton que leia 5 numeros e diga se cada um deles é PAR ou IMPAR

for i in range (1,6):
    num = int(input(f"Digite o {i}º numero "))
    resultado = "PAR" if num % 2 == 0 else "IMPAR"
    print(f"Entrada {i}: {num} --> {resultado}")


#for i in range (0,5):
#    num = int(input(f"digite o {i} numero: "))
#if num % 2 == 0:
#    print(f"({num} é PAR")
#else:
#    print(f"{num} é IMPAR")

