import math
#Obs: Em todas as funçoes epsilon é a tolerancia, o i é o numero de iterações e o maxIt é o maximo de iterações.
"A função bisseção implementa o metodo de bisseção para obter uma aproximação"
"da raiz de uma função matematica"
#Ela recebe como parametros uma função, e o intervalo que se inicia em a e termina no b.
def bissecao(f, a,b,epsilon=10**-15,maxIt = 50,i=1,Lr=[],Li=[]):
    x1=(a+b)/2 #aproxima da raiz da função
    erro=abs(a-b)/2#erro relativo
    print("{0:2d} [{1:.15f}] [{2:.15f}]".format(i, x1, erro))
    "imprime os valores enquanto x1 se aproxima da raiz da função" 
    if f(x1)==0 or erro<epsilon or i>maxIt:
        return Lr,Li #A função retorna uma lista com as aproximações da raiz e outra com o numero de iterações
    elif f(a)*f(x1)<0:
        return bissecao(f, a,x1,epsilon, maxIt,i+1,Lr+[x1],Li+[i])#Adiciona recursivamente os valores na lista
    else:
        return bissecao(f, x1,b,epsilon, maxIt,i+1,Lr+[x1],Li+[i])#Adiciona recursivamente os valores na lista

"A função raphson implementa método de Newton-Raphson usa a inclinaçãoda reta tangente dafunção f1 na"
"solução iterativa atual(xi) para encontrar a solução(xi+1) na próxima iteração. "
#Ela recebe como parametro a funçao (f1), sua derivada (f2) e um valor do intervalo [a,b]
def raphson(f1,f2,x1,i=1,epsilon=10**-15,maxIt=50,Lr=[],Li=[]):
    xi=x1-(f1(x1)/f2(x1))#aproxima da raiz da função
    erro=abs((xi-x1)/xi)#erro relativo
    print("{0:2d} [{1:.15f}] [{2:.15f}]".format(i,xi,erro))
    if f1(x1)==0 or f2(x1)==0 or xi==0 or erro<epsilon or i>maxIt:
        return Lr,Li #A função retorna uma lista com as aproximações da raiz e outra com o numero de iterações
    else:
        return raphson(f1,f2,xi,i+1,epsilon,maxIt,Lr+[],Li+[])#Adiciona recursivamente os valores na lista
    
"O método da Secante é uma variação do método de Newton-Raphson, evitando a necessidade de conhecer a derivada analítica de f1." 
#Os parametros são a função f1,e x1 e x2, valores do intervalo [a,b]
def secante(f1,x1,x2,i=1,epsilon=10**-15,maxIt=50,Lr=[],Li=[]):
    xi = x2 - f1(x2)*(x2 - x1)/(f1(x2) - f1(x1)) #aproxima da raiz da função
    erro=abs((xi-x2)/xi) #erro relativo
    print("{0:2d} [{1:.15f}] [{2:.15f}]".format(i, xi, erro))
    if f1(xi)==0 or erro<epsilon or i>maxIt:
        return Lr,Li #A função retorna uma lista com as aproximações da raiz e outra com o numero de iterações
    else:
        return secante(f1,x2,xi,i+1,epsilon, maxIt,Lr+[xi],Li+[i])#Adiciona recursivamente os valores na lista
    
"A função main irá fazer a chamada das funçoes que farão os calculos atraves dos metodos."
def main():
	funcao1=lambda x:x*(math.sin(x)) #recebe a função para que seja utilizada como parametro nas outras funçoes
	funcao2=lambda x:(math.sin(x))+x*(math.cos(x)) #recebe a derivada da função
	a=2 #primeiro valor do intervalo
	b=4 #ultimo valor do intervalo
	print("-"*45)
	print("Função escolhida: x*sen(x)")
	print("Derivada da função:f'(x)=sen(x)+x*cos(x)")
	print("\nNúmero máximo de iterações: 50")
	print("Tolerância (episilon):10**-15")
	print("-"*45)
	print("==> METÓDO DA BISSEÇÃO: x1={} e x2={}". format(a,b))
	print("-"*45)
	print("i            raiz             erro")
	print("-"*45)
	L1,L2=bissecao(funcao1,a,b)#chama a funcao bissecao
	print("-"*45)
	print("==> METÓDO DE NEWTON-RAPHSON: x1={}". format(b))
	print("-"*45)
	print("i            raiz             erro")
	print("-"*45)
	L3,L4=raphson(funcao1,funcao2,b)#chama a funcao raphson
	print("-"*45)
	print("==> METÓDO DA SECANTE: x1={} e x2={}". format(a,b))
	print("-"*45)
	print("i            raiz             erro")
	print("-"*45)
	L5,L6=secante(funcao1,a,b)#chama a funçao secante
main()
