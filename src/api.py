from app import app
from utils import jsonify, get_data


@app.route('/api/v1/data', methods=['GET'])
@jsonify
def data():
    return get_data()


@app.route('/api/v1/categories', methods=['GET'])
@jsonify
def categories():
    return [
        {'id': key, 'name': name}
        for key, name in get_data()['categories'].items()
    ]


@app.route('/api/v1/category/<int:category>', methods=['GET'])
@jsonify
def category_data(category):
    return [
        (country, values[category])
        for country, values in get_data()['countries'].items()
        if values[category]
    ]
