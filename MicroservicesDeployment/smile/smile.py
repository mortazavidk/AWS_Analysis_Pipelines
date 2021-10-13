from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
        ((Smile))-,
        ((sMile))-,
        ((smIle))-!
    """


@app.route('/echo_request')
def echo_request():
    return jsonify(dict(request.headers))


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
