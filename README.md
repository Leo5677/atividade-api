# ATIVIDADE API - LEONARDO VALENSOELA
#### Atividade final da disciplina API Gateway &amp; Integration

## Como testar?
#### 1. Acesse a pasta raíz do projeto através do console
#### 2. Utilize os comandos abaixo:
#### 3. 'docker build -t atividade-api .'
#### 4. 'docker run -p 8000:8000 atividade-api'
#### 5. Caso queira acessar a administração do sistema geral http://127.0.0.1:8000/admin/, utilize: Usuário: impacta | Senha: 123
#### 6. Caso queira acessar a administração do sistema de API do Django Rest: http://127.0.0.1:8000/api/v1/os/

## Tecnologias
#### 1. Python
#### 2. Django
#### 3. Django Rest Framework
#### 4. Banco de Dados SQLite3

## Entrega
#### 1. Implementação dos endpoints
#### 2. Banco de dados 
#### 3. Paginação para os endpoints 
(Basta acessar http://127.0.0.1:8000/api/v1/os/ce0ebd3f-a980-4be2-818d-755a93a884bb/equipamento/, por exemplo, para visualizar a paginação e filtros que o próprio Django Rest oferece)
#### 4. Há um arquivo chamado "API.postman_collection.json" na pasta raíz do projeto, que contém todos os endpoints com os payloads para testes
