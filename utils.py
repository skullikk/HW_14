import sqlite3


def get_film_title(query_title):
    """
    Функция получения самого нового фильма по слову в названии
    :param query_title: str
    :return: list[tuple]
    """
    with sqlite3.connect('./netflix.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                     SELECT *
                     FROM netflix
                     WHERE title LIKE ?
                     AND type = 'Movie'
                     ORDER BY release_year DESC
                     LIMIT 1
                     """, ("%"+query_title+"%",))
        film = cursor.fetchall()
        film_execute = {'title': film[0][2], 'country': film[0][5], 'release_year': film[0][7], 'genre': film[0][11],
                        'description': film[0][12]}
    return film_execute


def get_films_from_to_years(year_from, year_to):
    """
    Функция получения списка из 10 фильмов, вышедших между годами
    :param year_from: int
    :param year_to: int
    :return: list[tuple]
    """
    with sqlite3.connect('./netflix.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                        SELECT title, release_year
                        FROM netflix
                        WHERE release_year BETWEEN ? AND ?
                        AND type = 'Movie'
                        LIMIT 10
                        """, (year_from, year_to))
        films = cursor.fetchall()
        films_list = []
        for film in films:
            films_execute = {'title': film[0], 'release_year': film[1]}
            films_list.append(films_execute)
    return films_list


def get_films_by_rating(query_rating):
    """
    Функция получения списка из 10 фильмов по определенному рейтингу
    :param query_rating: str
    :return: list[tuple]
    """
    with sqlite3.connect('./netflix.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                        SELECT title, rating, description
                        FROM netflix
                        WHERE rating = ?
                        LIMIT 10
                        """, (query_rating,))
        films = cursor.fetchall()
        films_list = []
        for film in films:
            films_execute = {'title': film[0], 'rating': film[1], 'description': film[2]}
            films_list.append(films_execute)
    return films_list


rating_dict = {'children': ['G'], 'family': ['G', 'PG', 'PG-13'], 'adult': ['R', 'NC-17']}


def get_films_by_group_rating(group_rating):
    """
    Функция получения списка фильмов по определенной возрастной группе
    :param group_rating: str
    :return: list[tuple]
    """
    films_group_rating = []
    for rating in rating_dict[group_rating]:
        films_group_rating += get_films_by_rating(rating)
    return films_group_rating


def get_films_by_genre(query_genre):
    """
    Функция возвращает список из 10 последних фильмов по жанру
    :param query_genre: str
    :return: list[tuple]
    """
    with sqlite3.connect('./netflix.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                        SELECT title, listed_in, description, release_year
                        FROM netflix
                        WHERE type = 'Movie'
                        AND listed_in LIKE ?
                        ORDER BY release_year DESC
                        LIMIT 10
                        """, ("%"+query_genre+"%",))
        films = cursor.fetchall()
        films_list = []
        for film in films:
            films_execute = {'title': film[0], 'description': film[2]}
            films_list.append(films_execute)
    return films_list
