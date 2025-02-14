# API de Gerenciamento de Empresas e Obrigações Acessórias

Uma API simples desenvolvida com FastAPI para cadastro de empresas e gestão de obrigações acessórias declarativas ao governo.

## Tecnologias Utilizadas

- **FastAPI**: Framework para construção da API
- **SQLAlchemy**: ORM para interação com o banco de dados
- **PostgreSQL**: Banco de dados relacional
- **Pydantic**: Validação de dados e serialização
- **Uvicorn**: Servidor ASGI para execução da aplicação
- **pytest**: Realização de testes automatizados

## Pré-requisitos

- Python 3.8+
- PostgreSQL instalado e rodando
- Bibliotecas listadas em `requirements.txt`

## Configuração Inicial

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd [NOME_DO_DIRETORIO]
   python -m venv venv
2. Crie e ative um ambiente virtual:
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
3.Instale as dependências:
  ```bash
   pip install -r requirements.txt
```
4 Configure o banco de dados:
Crie um banco fastapi no PostgreSQL.
Confira as credenciais no arquivo .env

5. Execute a aplicação:
   ```bash
   uvicorn main:app --reload
    ```

