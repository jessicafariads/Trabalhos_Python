from os import system, name
def limpaTela():
    if name=='nt':
        system('cls')
    else:
        system('clear')
    
#A função inserir recebe como parâmetro o preço do produto escolhido na função maquina, e retorna o troco que o usuário deve receber...
        
def inserir(pre,y=0,q=0):
    x=float(input("\nColoque o dinheiro: "))
    if x>=pre:
        print("Valor pago:{}". format(x))
        t=x-pre
        print("Troco:{}".format (round(t,2)))
        if t>0:
            print("\nPegue seu troco...")
        else:
            print("Não há troco")
        if t>=1:
            y=round(100*(t-int(t)))
            troco(t,y)
        elif t>0.10:
            y=round(t*100)
            troco(t,y)
        else:
            y=round(t,2)*100
            troco(t,y)
    elif q+x>=pre:
        print("\nValor pago:{}". format(q+x))
        t=(q+x)-pre
        print("Troco:{}".format (round(t,2)))
        if t>0:
            print("\nPegue seu troco...")
        else:
            print("Não há troco")
        if t>=1:
            y=round(100*(t-int(t)))
            troco(t,y)
        elif t>0.10:
            y=round(t*100)
            troco(t,y)
        else:
            y=round(t,2)*100
            troco(t,y)
    else:
        return inserir(pre,y,q+x)
    
    
#Essa função recebe a parte decimal do troco multiplicado pr 100 e imprime os valores na tela, depois retorna para a função anterior
    
def tadificil(y):
    if y==0:
        return
    elif y<=4:
        print("R$0.01")
        return tadificil(y-1)
    elif y<10:
        print("R$0.05")
        return tadificil(y-5)
    elif y<25:
        print("R$0.10")
        return tadificil(y-10)
    elif y<50:
        print("R$0.25")
        return tadificil(y-25)
    else:
        print("R$0.50")
        return tadificil(y-50)
        
#A função troco recebe dois parametros y, que é a parte decimal do troco multiplicada por 100, e x que é o valor total do troco...
#Ela imprime recursivamente o valor do troco na tela.
    
def troco(x,y):
    w=int(x)
    if w==0:
        if y==0:
            return
        else:
            return tadificil(y)
    elif w<2:
        print("R$1.00")
        return troco(w-1,y)
    elif w<5:
        print("R$2.00")
        return troco(w-2,y)
    elif w<10:
        print("R$5.00")
        return troco(w-5,y)
    elif w<20:
        print("R$10.00")
        return troco(w-10,y)
    elif w<50:
        print("R$20.00")
        return troco(w-20,y)
    elif w<100:
        print("R$50.00")
        return troco(w-50,y)
    else:
        print("R$100.00")
        return troco(w-100,y)

    
#A função maquina recebe 5 parametros referentes ao estoque da máquina e o parametro "s" que recebe valor no momento que a função é chamada.
#"s" representa o estoque da maquina e enquanto s>0 a maquina pode continuar funcionando a não ser que o cliente não queira continuar a compra.
#Ela imprime as opçoes na tela, recebe a opção escolhida pelo usuario e chama a função inserir que recebe como parametro o preço do produto escolhido.
#Ao termino da entrega do troco ela perguntara ao usuario se ele quer continuar e se sim vai chamar a si mesma e diminuirá o estoque...
    
def maquina(a,b,c,d,e,s=0):
    s=a+b+c+d+e
    if s>0:
        limpaTela()
        print("-"*48)
        print("-------- A FANTASTICA MÁQUINA DE COMIDA --------")
        print("-"*48)
        if a>0:
            print("1 - Ruffles     - R$3.75")
        else:
            print("1 - Ruffles     - Indisponível")
        if b>0:
            print("2 - Coca-cola   - R$2.49")
        else:
            print("2 - Coca-cola   - Indisponível")
        if c>0:
            print("3 - Red Bull    - R$4.99")
        else:
            print("3 - Red Bull    - Indisponível")
        if d>0:
            print("4 - Paçoca      - R$0.50")
        else:
            print("4 - Paçoca      - Indisponível")
        if e>0:
            print("5 - Jujuba      - R$0.75")
        else:
            print("5 - Jujuba      - Indisponível")
        print("-"*48)
        op=int(input("Escolha seu produto: "))
        if op==1:
            if a>0:
                print("Você escolheu Ruffles")
                print("Preço: R$3.75")
                valorP=3.75
            else:
                print("Desculpe,mas o Ruffles está indisponível")
                return escolha(a,b,c,d,e,s)
        elif op==2:
            if b>0:
                print("Você escolheu Coca-Cola")
                print("Preço:R$2.49")
                valorP=2.49
            else:
                print("Desculpe,mas a Coca-Cola está indisponível")
                return escolha(a,b,c,d,e,s)
        elif op==3:
            if c>0:
                print("Você escolheu Red Bull")
                print("Preço:R$4.99")
                valorP=4.99
            else:
                print("Desculpe, mas o Red Bull está indisponível")
                return escolha(a,b,c,d,e,s)
        elif op==4:
            if d>0:
                print("Você escolheu Paçoca")
                print("Preço:R$0.50")
                valorP=0.50
            else:
                print("Desculpe, mas a Paçoca está indisponível")
                return escolha(a,b,c,d,e,s)
        elif op==5:
            if e>0:
                print("Você escolheu Jujuba")
                print("Preço:R$0.75")
                valorP=0.75
            else:
                print("Desculpe, mas a Jujuba está indisponível")
                return escolha(a,b,c,d,e,s)
        else:
            print("Opção Invalida")
            return maquina(a,b,c,d,e,s)
        inserir(valorP)
        print("-"*48)
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
            print("Obrigado pela preferencia.")
            print("Volte sempre!!!")
            print("E que a Força esteja com você!")
            return exit
    else:
            print("Desculpa, mas a máquina está sem produtos.")
            return exit

#E por ultimo mas não menos importante tem a função escolha que vai perguntar ao usuario se ele quer continuar a utilizar a maquina.
#Se sim vai chamar a função maquina novamente.

def escolha(a,b,c,d,e,s):
    s=a+b+c+d+e
    i=input("\nDeseja escolher outro produto?(S/N): ")
    if i=="s" or i=="S":
        return maquina(a,b,c,d,e)
    else:
        return exit

    
    
maquina(1,5,5,5,5)
        
            
            
