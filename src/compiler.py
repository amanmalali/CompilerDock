from quart import Blueprint, jsonify, request
from quart.exceptions import HTTPException

from src.utils.run import run_code

compiler_bp = Blueprint("compiler", __name__)


@compiler_bp.route("/", methods=["POST"])
async def compiler():
    req_data = await request.get_json()
    lang = req_data["lang"]
    code = req_data["code"]
    id_no = req_data["id"]
    stdin = req_data["stdin"]
    try:
        output, error, fail, timeout_flag = await run_code(lang, code, stdin)
    except HTTPException as http_err:
        return {"error": http_err.description}, http_err.status_code

    send_res = {
        "output": output,
        "error": error,
        "fail": fail,
        "timeout": timeout_flag,
        "id": id_no,
    }
    HTTPException
    return jsonify(send_res)
