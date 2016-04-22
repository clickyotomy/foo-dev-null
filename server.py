#! /usr/bin/env python2.7

'''
Take what you can, give nothing back.
'''

from flask import Flask, request

app = Flask(__name__)


@app.route('/dev/null', methods=['GET', 'POST'])
def serve():
    if request.method == 'GET':
        return ('', 204)
    if request.method == 'POST':
        return ('', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
