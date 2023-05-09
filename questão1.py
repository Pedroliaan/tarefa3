num = int(input("insira um número inteiro (digite 0 para finalizar)"))
cont = 0 
total = 0 

while num != 0:
    cont = cont + 1
    total = total + num
    num = int(input("insira um número inteiro (digite 0 para finalizar)"))

print("soma do total: ", total, "Média de tudo: ", total/cont)