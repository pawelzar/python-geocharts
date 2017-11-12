from flask.json import jsonify

from app import app
from utils import get_data


@app.route('/api/v1/data', methods=['GET'])
def data():
    return jsonify(get_data())


@app.route('/api/v1/categories', methods=['GET'])
def categories():
    return jsonify([
        {'id': key, 'name': name}
        for key, name in get_data()['categories'].items()
    ])


@app.route('/api/v1/category/<int:category>', methods=['GET'])
def category_data(category):
    return jsonify([
        (country, values[category])
        for country, values in get_data()['countries'].items()
        if values[category]
    ])
