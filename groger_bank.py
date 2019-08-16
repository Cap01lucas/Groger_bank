print("Bem vindo ao banco GrogerBank, Cadastre-se:")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sim = float(input("Digite o valor da simulação de saldo: "))

contador = sim

x = float(input("qual operação da sua escolha:\n"
        "1-Saque \n"
        "2-Deposito \n" 
        "3-Emprestimo \n" 
        "4-Para visualizar informações \n" 
        "Aperte qualquer outro para sair: "))
if (x == 1):
    def saque(x, contador):
        sq = float(input("Valor de saque: "))
    
        if sq <= contador:
            print (nome, idade)
            saldo = print("Saldo:",contador - sq )
        else:
            print("Saldo a baixo")

        return = saldo
saque(contador, x)    

elif (x == 2):
    def deposito(2, contador):
        dp = float(input("Valor de deposito: "))
        if dp <= 5000:
            print (nome, idade)
            print("Saldo:",contador + dp )
        else :
            print("Valor acima do limite")

        contador = saldo
deposito(x,contador)

# elif x == 3:
#     em = float(input("Valor de Emprestimo: "))
#     print (nome, idade)
#     print("Saldo:",contador + em )

            


