tab= int(input("Digite o numero desejado: "))
print(f"Taboada do numero {tab} ")
x=0
while x <= 10:
    v = x * tab
    print(f"{tab} x {x} = {v}")
    x = x + 1
