#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#TODO- 1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra

response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

# Resposta:
# produtos_acima_30 = [
#     {
#         "nome": loja["nome"],
#         "endereço": loja["endereço"],
#         "produtos": [produto for produto in loja["produtos"] if produto["preço"] > 30]
#     }
#     for loja in response
# ]
# print(produtos_acima_30)

#TODO- 2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

#Resposta:
# preco_produto_b = next(produto["preço"] for produto in responsejson["produtos"] if produto["nome"] == "Produto B")
# print("Produto B: ", preco_produto_b)


#TODO- 3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

#Resposta:
# lista_ordenada = sorted(lista)
# print(lista_ordenada)


#TODO- 4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela


lista = ["   joao   ","   maria   ","  joana  "]

#Resposta:
# lista_sem_espacos = [nome.strip() for nome in lista]
# print(lista_sem_espacos)

#TODO- 5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

#Resposta:
# lista.pop(1)
# print(lista)

#TODO- 6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

#Resposta:
# nova_lista = ["maria" if nome == "joao" else nome for nome in lista]
# print(nova_lista)

#TODO- 7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra



#TODO- 8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

#Resposta:
# import requests
# def contar_tasks():
#     response = requests.get('https://jsonplaceholder.typicode.com/todos')
#     tasks = response.json()
#     completadas = sum(1 for task in tasks if task['completed'])
#     pendentes = len(tasks) - completadas
#     return completadas, pendentes
# print(contar_tasks())

#TODO- 9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra

#Resposta:
# import requests
# def obter_dados_usuarios():
#     response = requests.get('https://jsonplaceholder.typicode.com/users')
#     usuarios = response.json()
#     dados_extraidos = [
#         {
#             "nome": usuario["name"],
#             "username": usuario["username"],
#             "email": usuario["email"],
#             "rua": usuario["address"]["street"],
#             "numero": usuario["address"]["suite"]
#         }
#         for usuario in usuarios
#     ]
#     return dados_extraidos
# print(obter_dados_usuarios())


#TODO-10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

#Resposta:
# lista_fifo = []
# lista_fifo.append("Novo item")
# print(lista_fifo)

#TODO- 11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

#Resposta:
# lista_lifo = []
# lista_lifo.append("Novo item")
# print(lista_lifo.pop()) 


#TODO- DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

