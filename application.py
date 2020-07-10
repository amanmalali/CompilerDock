from flask import Flask
from flask_cors import CORS, cross_origin

from src.compiler import compiler_bp

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(compiler_bp)


if __name__ == '__main__':
	app.run(debug=True)
