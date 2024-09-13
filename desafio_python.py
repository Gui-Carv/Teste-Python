#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta


class ContaBancaria:

    contador_id = 1
    
    def __init__(self, nome, cpf):
        self.id = ContaBancaria.contador_id
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0    #Saldo inicia em 0
        ContaBancaria.contador_id += 1  #ID autoincremental

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saque não realizado. Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

def interface_banco():
    contas = [] #Lista para armazenar conta criada
    
    while True:
        print("\n=== Bem-vindo! ===")
        print("1. Criar nova conta")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Consultar saldo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            nova_conta = ContaBancaria(nome, cpf)
            contas.append(nova_conta)
            print(f"Conta criada com sucesso! Seu ID é {nova_conta.id}")
        
        elif opcao == '2':
            id_conta = int(input("Digite o ID da conta: "))
            conta = next((c for c in contas if c.id == id_conta), None)
            if conta:
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")
        
        elif opcao == '3':
            id_conta = int(input("Digite o ID da conta: "))
            conta = next((c for c in contas if c.id == id_conta), None)
            if conta:
                valor = float(input("Digite o valor para saque: "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")
        
        elif opcao == '4':
            id_conta = int(input("Digite o ID da conta: "))
            conta = next((c for c in contas if c.id == id_conta), None)
            if conta:
                conta.consultar_saldo()
            else:
                print("Conta não encontrada.")
        
        elif opcao == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    interface_banco()   #Executa a interface do banco
