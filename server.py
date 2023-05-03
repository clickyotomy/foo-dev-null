#!/usr/bin/env python3

"""
/dev/null: Take what you can, give nothing back.
"""

from flask import Flask, request, url_for, redirect

app = Flask(__name__)
methods = [
    "HEAD",
    "GET",
    "OPTIONS",
    "TRACE",
    "CONNECT",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
]


@app.errorhandler(404)
def dev_null_redirect(_):
    """
    Redirect everything to `/dev/null'.
    """
    return redirect(url_for("serve"))


@app.route("/dev/null", methods=methods)
def serve():
    """
    This is the default route. Doesn't do anything.
    """
    if request.method in ["POST", "PUT", "PATCH"]:
        return ("", 204)

    return ("", 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
