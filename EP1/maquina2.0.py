def inserir(pre):
    x=float(input("\nColoque o dinheiro: "))
    print("Valor pago:{}". format(x))
    t=x-pre
    print("Troco:{}".format (t))
    print("\nPegue seu troco...")
    troco(t)
        
    
def troco(x):
    if x==0:
        return
    elif x==1:
        print("R$1.00")
        return troco(x-1)
    elif x<5:
        print("R$2.00")
        return troco(x-2)
    elif x<10:
        print("R$5.00")
        return troco(x-5)
    elif x<20:
        print("R$10.00")
        return troco(x-10)
    elif x<50:
        print("R$20.00")
        return troco(x-20)
    elif x<99:
        print("R$50.00")
        return troco(x-50)
    else:
        print("R$100")
        return troco(x-100)
        
def maquina(a,b,c,d,e,s=0):
    s=a+b+c+d+e
    if s>0:
        print("-"*40)
        if a>0:
            print("1 - Ruffles     - R$4.00")
        else:
            print("1 - Ruffles     - Indisponível")
        if b>0:
            print("2 - Coca-cola   - R$2.00")
        else:
            print("2 - Coca-cola   - Indisponível")
        if c>0:
            print("3 - Red Bull    - R$5.00")
        else:
            print("3 - Red Bull    - Indisponível")
        if d>0:
            print("4 - Paçoca      - R$1.00")
        else:
            print("4 - Paçoca      - Indisponível")
        if e>0:
            print("5 - Jujuba      - R$2.00")
        else:
            print("5 - Jujuba      - Indisponível")
        print("-"*40)
        op=int(input("Escolha seu produto: "))
        if op==1:
            if a>0:
                print("Você escolheu Ruffles")
                print("Preço: R$4.00")
                valorP=4.00
            else:
                print("Desculpe mas o Ruffles está indisponível")
                return escolha(a,b,c,d,e,s)
        elif op==2:
            if b>0:
                print("Você escolheu Coca-Cola")
                print("Preço:R$2.00")
                valorP=2.00
            else:
                print("Desculpe mas a Coca-Cola está indisponível")
                return escolha(a,b,c,d,e,s)
        elif op==3:
            if c>0:
                print("Você escolheu Jujuba")
                print("Preço:R$5.00")
                valorP=5.00
            else:
                print("Desculpe mas a Jujuba está indisponível")
                return escolha(a,b,c,d,e,s)
        elif op==4:
            if d>0:
                print("Você escolheu Paçoca")
                print("Preço:R$1.00")
                valorP=1.00
            else:
                print("Desculpe mas a Paçoca está indisponível")
                return escolha(a,b,c,d,e,s)
        elif op==5:
            if e>0:
                print("Você escolheu Jujuba")
                print("Preço:R$2.00")
                valorP=2.00
            else:
                print("Desculpe mas o produto está indisponível")
                return escolha(a,b,c,d,e,s)
        else:
            print("Opção Invalida")
            return maquina(a,b,c,d,e,s)
        inserir(valorP)
        print("-"*40)
        i=input("Deseja escolher outro produto?(S/N): ")
        if i=="s" or i=="S":
            if op==1:
                return maquina(a-1,b,c,d,e)
            elif op==2:
                return maquina(a,b-1,c,d,e)
            elif op==3:
                return maquina(a,b,c-1,d,e)
            elif op==4:
                return maquina(a,b,c,d-1,e)
            else:
                return maquina(a,b,c,d,e-1)
        else:
            return exit
    else:
            print("Desculpa, mas a máquina está sem produtos.")
            return exit

def escolha(a,b,c,d,e,s):
    s=a+b+c+d+e
    i=input("\nDeseja escolher outro produto?(S/N): ")
    if i=="s" or i=="S":
        return maquina(a,b,c,d,e)
    else:
        return exit

    
    
maquina(1,1,1,1,1)
        
            
            
