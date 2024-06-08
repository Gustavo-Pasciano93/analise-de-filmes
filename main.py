import requests
import sqlite3

def fetch_movie_data(movie_title):
    api = "http://www.omdbapi.com/?i=tt3896198&apikey=63b84943"

    response = requests.get(api)
    response.raise_for_status()
    return response.json()

movie_title = "Guardians of the Galaxy Vol. 2"
movie_data = fetch_movie_data(movie_title)
    


conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

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


def insert_movie_data(cursor, movie_data):
    cursor.execute('''
    INSERT INTO movies (title, year, genre, director, actors, plot, imdb_rating) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (movie_data['Title'], movie_data['Year'], movie_data['Genre'], movie_data['Director'], movie_data['Actors'], movie_data['Plot'], movie_data['imdbRating']))
    conn.commit()

insert_movie_data(cursor, movie_data)

# Verificação dos dados inseridos
cursor.execute('SELECT * FROM movies')
print(cursor.fetchall())

# Fechamento da conexão
conn.close()
