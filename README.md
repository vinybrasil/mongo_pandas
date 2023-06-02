# Mongo - Pandas - Docker

## Introdução
Repositório com um script python que lê dois arquivos CSV e cria um DataFrame Pandas com
o mesmo. Depois, faz o upload dos dados para uma base de dados MongoDB, especificamente 
numa database com o nome de "cars" e cria duas collections: "Carros" e "Montadoras". Após 
tal feito, o script roda uma pipeline para agrupar os dados com base no país da montadora
e cria uma nova collection com a id como a montadora e o payload com os carros daquela montadora.

## Como rodar

```bash
docker-compose up
```

## Questionário
Não tive dificuldades na execução da tarefa. O único problema foi o tempo curto, o que 
impediu de fazer testes unitários para todas as funções e criar uma API CRUD para 
interagir melhor com a base de dados.
No que tange às minhas esperiências, nunca usei Pentaho e uso mongodb há aproximadamente 6 meses. Embora seja um tempo curto, como já trabalho há quase três anos com DynamoDB, não tive problemas com tal base NoSQL. Tenho pouca experiência com ETL mas estou disposto à aprender. No que tange à Python, tenho conhecimento avançado, indo desde testes unitários até paralelismo.

