# CineFlow API

CineFlow API é o backend para um sistema de gerenciamento de cinema, desenvolvido em Python com o framework FastAPI. A aplicação permite o cadastro e controle de filmes, salas, sessões de exibição e a venda de ingressos.

## Funcionalidades

- **Gerenciamento de Filmes:** Endpoints para criar, listar, atualizar e deletar filmes do catálogo.
- **Gerenciamento de Salas:** Endpoints para o controle total das salas do cinema, incluindo nome e capacidade.
- **Agendamento de Sessões:** Sistema completo para agendar sessões, com uma lógica robusta que impede o agendamento em horários conflitantes na mesma sala.
- **Venda de Ingressos:** Endpoint para "comprar" um ingresso para uma sessão específica, com validação para impedir a venda de assentos já ocupados.
- **Consulta de Dados:** Rotas para listar todos os recursos cadastrados e para visualizar os ingressos vendidos por sessão.

## Tecnologias Utilizadas

- **Backend:** Python, FastAPI
- **Banco de Dados:** SQLite com SQLAlchemy

## Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto localmente:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/ArthurDOli/CineFlow.git
    cd CineFlow
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Crie o banco de dados:**
    Este projeto utiliza SQLite e não requer configuração de variáveis de ambiente. Para criar o banco de dados inicial, execute o script:

    ```bash
    python database.py
    ```

5.  **Execute a aplicação:**
    ```bash
    uvicorn main:app --reload
    ```
    A API estará disponível com a documentação interativa em `http://127.0.0.1:8000/docs`.

## Estrutura do Projeto

```
CineFlow/
├── routers/
│ ├── movie.py
│ ├── room.py
│ ├── session.py
│ └── ticket.py
├── .gitignore
├── database.py
├── dependencies.py
├── main.py
├── models.py
├── schemas.py
└── requirements.txt
```

- **main.py:** Ponto de entrada da aplicação FastAPI, onde os roteadores são incluídos.
- **database.py:** Script para inicializar o banco de dados.
- **dependencies.py:** Define dependências reutilizáveis, como a sessão do banco de dados.
- **models.py:** Define os modelos de dados do SQLAlchemy (tabelas do banco de dados).
- **schemas.py:** Define os schemas do Pydantic para validação de dados de entrada e saída.
- **routers/:** Contém os arquivos que definem os endpoints da API, agrupados por recurso.
