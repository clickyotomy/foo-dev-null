#! /usr/bin/env python3

'''
/dev/null -- Take what you can, give nothing back.
'''

from flask import (Flask, request, url_for, redirect)

APP = Flask(__name__)
METHODS = [
    'GET', 'HEAD', 'POST', 'PUT', 'DELETE',
    'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'
]

@APP.errorhandler(404)
def dev_null_redirect(err):
    '''
    Redirect everything to `/dev/null'.
    '''
    return redirect(url_for('serve'))


@APP.route('/dev/null', methods=METHODS)
def serve():
    '''
    This is the default route. Doesn't do anything.
    '''
    if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
        return ('', 200)

    return ('', 204)



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=False)
