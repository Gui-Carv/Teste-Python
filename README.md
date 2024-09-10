# Teste-Python

## Explicação para as respostas:

### 1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 

Eu percorri cada loja e filtrei os produtos dessa loja usando uma list comprehension. Escolhi essa abordagem porque é simples e direta, e permite acessar e manipular rapidamente os dados.

### 2- Use o JSON abaixo para capturar o preço do produto B

Usei a função next com uma expressão geradora para obter o preço do Produto B. Essa solução é eficiente porque percorre a lista de produtos e retorna o valor assim que encontra o item desejado.

### 3- Ordene a lista abaixo em ordem crescente

Utilize sorted para ordenar a lista em ordem crescente. Essa função cria uma nova lista ordenada sem modificar a original.

### 4- Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

Usei strip em uma list comprehension para remover os espaços em branco, resultando em uma nova lista sem espaços extras.

### 5- Retire o segundo item dessa lista e imprima ela

Usei pop(1) para remover o segundo item da lista.

### 6- Substitua todos os "joao" da lista por "maria"

Usei uma list comprehension com uma expressão condicional para substituir o nome, assim consegui criar uma lista nova onde todo nome joão é alterado por maria.

### 7- Crie um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1

Infelizmente não compreendi muito bem a questão e não consegui realizar. 

### 8- Usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. Cada objeto dentro do json possui a chave "completed", que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes

Usei requests para fazer uma requisição HTTP e depois processei a resposta JSON para contar tasks completadas e pendentes.

### 9- Faça uma requisição em uma API https://jsonplaceholder.typicode.com/users e com os dados retornados faça um parsing de dados e retire o nome, username, email, rua, numero

Novamente usei o requests para uma requisição HTTP para obter dados de usuários e usei uma list comprehension para extrair nome, username, email, rua e número.

### 10- Crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

Criei uma lista e adicionei um item novo usando o método append. É um método adequado para implementar a abordagem FIFO, pois adiciona o item ao final da lista, preservando a ordem de inserção.

### 11- Crie uma lista e adicione um item novo a ela utilizando a metodologia LIFO

Criei uma lista e adicionei um item usando append, e depois removi com pop. Representando a abordagem LIFO (Last In, First Out), onde o último item adicionado é o primeiro a ser removido.
