import json
import sqlite3


def get_actors(first_actor, second_actor):
    """
    Фукция вывода списка артисктов, которые сыграли с введенными двумя актерами более 2 раз
    :param first_actor: str
    :param second_actor: str
    :return: actors_all_1: list[str]
    """
    with sqlite3.connect('./netflix.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                    SELECT netflix.cast
                    FROM netflix
                    WHERE netflix.cast LIKE ?
                    AND netflix.cast LIKE ?
                    """, ("%"+first_actor+"%", "%"+second_actor+"%"))
        films = cursor.fetchall()
        actors = []
        for film in films:
            actors += film[0].split(', ')
        actors_all = []
        for actor in actors:
            if actors.count(actor) >= 2:
                actors_all.append(actor)
        actors_all_1 = set(actors_all)
        actors_all_1.remove(first_actor)
        actors_all_1.remove(second_actor)
    return actors_all_1


def get_films_with_description(type, release_year, genre):
    """
    Функция вывода json записи фильмов по из виду.ю году и жанру
    :param type: str
    :param release_year: int
    :param genre: str
    :return: json
    """
    with sqlite3.connect('./netflix.db') as con:
        cursor = con.cursor()
        cursor.execute("""
                    SELECT title, description
                    FROM netflix
                    WHERE type LIKE ?
                    AND release_year = ?
                    AND listed_in LIKE ?
                    """, ("%"+type+"%", release_year, "%"+genre+"%"))
        films = cursor.fetchall()
        films_list = []
        for film in films:
            films_execute = {'title': film[0], 'description': film[1]}
            films_list.append(films_execute)

    return json.dumps(films_list, ensure_ascii=False)

