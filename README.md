# API CRUD com Flask, Mongo e Docker

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
