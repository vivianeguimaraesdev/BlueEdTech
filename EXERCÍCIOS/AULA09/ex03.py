#PANIFICADORA

preço = float(input("PREÇO DO PÃO: "))
for n in range(1, 51):
    print(f'{n:>2} - R${n*preço:.2f}')