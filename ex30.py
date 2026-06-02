tab= int(input("Digite o numero desejado: "))
print(f"Taboada do numero {tab} ")
for i in range (0,11):
    v = tab * i 
    print(f"{tab} x {i} = {v}")