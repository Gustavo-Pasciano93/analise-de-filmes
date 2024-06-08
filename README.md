# Movie Data Pipeline

Este projeto consiste na criação de um pipeline de dados que coleta informações de filmes da API OMDb, armazena esses dados em um banco de dados SQLite e realiza análises básicas.

## Objetivo

O objetivo deste projeto é demonstrar a aplicação de conhecimentos em Python e SQL, bem como a integração de APIs em um pipeline de dados simples.

## Funcionalidades

- Coleta de dados de filmes usando a API OMDb
- Armazenamento dos dados em um banco de dados SQLite
- Criação de tabelas e inserção de dados no banco de dados
- Consulta e visualização dos dados armazenados

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `main.py`: Script principal que executa todas as etapas do pipeline de dados
- `README.md`: Este arquivo, contendo a documentação do projeto

## Requisitos

- Python 3.12
- Bibliotecas Python: `requests`, `sqlite3`

## Configuração e Execução

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/movie-data-pipeline.git
    cd movie-data-pipeline
    ```

2. Instale as dependências:
    ```bash
    pip install requests
    ```

3. Execute o script principal:
    ```bash
    python main.py
    ```

## Detalhes do Código

### Coleta de Dados

O script utiliza a função `fetch_movie_data` para buscar informações de um filme específico da API OMDb.

```python
import requests

def fetch_movie_data(movie_title):
    api_key = "sua_chave_api_aqui"
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

movie_title = "Guardians of the Galaxy Vol. 2"
movie_data = fetch_movie_data(movie_title)


### Armazenamento de Dados
Os dados coletados são armazenados em um banco de dados SQLite. A estrutura da tabela é definida e os dados são inseridos usando SQL.


import sqlite3

# Conexão ao banco de dados SQLite
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Criação da tabela de filmes
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    year TEXT,
    genre TEXT,
    director TEXT,
    actors TEXT,
    plot TEXT,
    imdb_rating TEXT
)
''')

# Inserção de dados na tabela
def insert_movie_data(cursor, movie_data):
    cursor.execute('''
    INSERT INTO movies (title, year, genre, director, actors, plot, imdb_rating) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (movie_data['Title'], movie_data['Year'], movie_data['Genre'], movie_data['Director'], movie_data['Actors'], movie_data['Plot'], movie_data['imdbRating']))
    conn.commit()

insert_movie_data(cursor, movie_data)




### Verificação de Dados

Os dados inseridos podem ser verificados com uma consulta simples.

# Verificação dos dados inseridos
cursor.execute('SELECT * FROM movies')
print(cursor.fetchall())

# Fechamento da conexão
conn.close()
