from dotenv import load_dotenv
from quart import Quart
from quart_cors import cors

from src.compiler import compiler_bp

load_dotenv(verbose=True)
app = Quart(__name__)
cors = cors(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.register_blueprint(compiler_bp)
