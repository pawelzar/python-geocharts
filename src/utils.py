import csv

import logging
log = logging.getLogger(__name__)  # pylint: disable=invalid-name


def get_data():
    """
    Extracts data from CSV file.

    It creates structure like this:
    data = {
        'categories': {
            0: 'First category',
            1: 'Second category',
        },
        'countries': {
            'Albania': {
                0: 50,
                1: 323,
            },
            'United States': {
                0: '',
                1: 12,
            },
        },
    }
    """
    data = {}
    with open('src/resources/data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data['categories'] = {
            i: category for i, category in enumerate(next(reader)[1:])
        }
        data['countries'] = {}
        for i, row in enumerate(reader):
            try:
                country = row[0]
                data['countries'][country] = {
                    category: validate_value(value)
                    for category, value in enumerate(row[1:])
                }
            except (ValueError, TypeError):
                log.debug('Problem with line %d: ', i, exc_info=True)

    return data


def validate_value(value):
    try:
        return float(value)
    except ValueError:
        return ''
