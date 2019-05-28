#! /usr/bin/env python3

'''
/dev/null -- Take what you can, give nothing back.
'''

from flask import Flask, request

APP = Flask(__name__)


@APP.route('/dev/null', methods=['GET', 'POST'])
def serve():
    '''
    This is the default route. Doesn't do anything.
    '''
    if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
        return ('', 200)

    return ('', 204)



if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=False)
