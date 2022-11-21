print("1-coca cola R$5.00")
print("2-agua R%2.00")
print("3-guarana R$4.50")
print("4-pepsi R$5.00")
print("5-sprit R$4.50")
escolha=int(input("estre com sua escolha entre 1-5"))
while escolha<1 or escolha>5:
    escolha=int(input("entre com a sua escolha novamente 1-5"))
valor=float(input("qual o valor colocado na maquina?:"))
    
if escolha==1:
    if valor>=5.00:
        saida1="coca cola"
        saida2=(valor-5.00)
    else:
        saida1=None
        saida2=valor
elif escolha==2:
    if valor >= 2.00:
        saida1="agua"
        saida2=(valor-2.00)
    else:
        saida1=None
        saida2=valor
elif escolha==3:
    if valor>=4.50:
        saida1="guarana"
        saida2=(valor-4.50)
    else:
        saida1=None
        saida2=valor
elif escolha==4:
    if valor>=5.00:
        saida1="pepsi"
        saida2= (valor-5.00)
    else:
        saida1=None
        saida2=valor
elif escolha==5:
    if valor>=4.50:
        saida1="sprite"
        saida2=(valor-4.50)
    else:
        saida1=None
        saida2=valor
else:
    print("esolha errada")
print(saida1)
print(saida2)



    
    
