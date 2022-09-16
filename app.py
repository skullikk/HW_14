from flask import Flask, jsonify
from utils import get_film_title, get_films_from_to_years, get_films_by_group_rating, get_films_by_genre

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/movie/<title>')
def search_film(title):
    return jsonify(get_film_title(title))


@app.route('/movie/<int:year_from>/to/<int:year_to>')
def page_films_between_years(year_from, year_to):
    return jsonify(get_films_from_to_years(year_from, year_to))


@app.route('/rating/<rating>')
def page_films_rating(rating):
    return jsonify(get_films_by_group_rating(rating))


@app.route('/genre/<genre>')
def page_films_genre(genre):
    return jsonify(get_films_by_genre(genre))


if __name__ == '__main__':
    app.run()
