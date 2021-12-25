from flask import Flask, jsonify
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = "<h3>Hi I am Flask</h3>"
    return html.format(format)
    
@app.route('/hi/<name>')
def hello(name):
    greeting = f"Hello: {name}"
    return jsonify(greeting)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
