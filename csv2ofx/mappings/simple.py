from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter

mapping = {
    'has_header': True,
    'is_split': False,
    'bank': 'Simple Bank',
    'currency': 'USD',
    'delimiter': ',',
    'account': 'Checking',
    'date': itemgetter('Date'),
    'amount': itemgetter('Amount'),
    'desc': itemgetter('Reference'),
    'payee': itemgetter('Description'),
    'notes': itemgetter('Memo'),
    'id': itemgetter('Row'),
}
