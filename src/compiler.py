from flask import Blueprint, jsonify, request

from src.utils.run import run_code

compiler_bp = Blueprint("compiler", __name__)

@compiler_bp.route('/', methods=['POST'])
def compiler():
	lang = request.json['lang']
	code = request.json['code']
	id_no = request.json['id']
	stdin = request.json['stdin']
	output, error, fail, timeout_flag = run_code(lang, code, stdin)	
	send_res={"output": output, "error": error, "fail": fail, "timeout": timeout_flag, "id": id_no}
	return(jsonify(send_res))

