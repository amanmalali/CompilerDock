#import docker
#import time
#client=docker.from_env().api
#container=client.create_container(image='compiler:v1', command='/bin/sleep 30')
#print(container)
from flask import Flask,jsonify,request
import os
import time
import shutil
from random import randint
import subprocess
from flask_cors import CORS, cross_origin
application = Flask(__name__)
cors=CORS(application)
application.config['CORS_HEADERS']='Content-Type'

comp=['c','c++']
inter={"python3":"python3","c":"gcc","c++":"g++","java":"java"}
filenames={"python3":"file.py","c":"file.c","c++":"file.cpp","java":"file.java"}

def create_files(data,filename,dest):
	file=open(dest+"/"+filename,"w")
	file.write(data)
	file.close

def copy_files(src,dest):
	src_files = os.listdir("./scripts/")
	for file_name in src_files:
		full_file_name = os.path.join(src, file_name)
		dest_file_name=os.path.join(dest,file_name)
		if os.path.isfile(full_file_name):
			shutil.copy(full_file_name, dest_file_name)

@application.route('/',methods=['POST'])
def compiler():
	sleep_count=0
	timeout=20
	lang=request.json['lang']
	code=request.json['code']
	id_no=request.json['id']
	stdin=request.json['stdin']
	folder_name=hex(randint(10000000,99999999))
	dest="./temp/"+folder_name
	src="./scripts"
	os.mkdir("./temp/"+folder_name)
	
	copy_files(src,dest)
	
	create_files(code,filenames[lang],dest)
	create_files(stdin,"input",dest)
	if(lang in comp):
		param2='./compile/script.sh '+inter[lang] +' '+filenames[lang]+' ./a.out'
	else:
		param2='./compile/script.sh '+inter[lang]+' '+filenames[lang]
	subprocess.call(['./dockerRun.sh',folder_name, param2])
	
	finish_run=False
	while sleep_count!=timeout and not finish_run:
		if os.path.exists(dest+"/completed"):
			finish_run=True
		else:
			time.sleep(1)
			sleep_count+=1

	file=open(dest+"/errors","r")
	error=file.read()
	file.close()
	if error == "":
		fail=0
	else:
		fail=1

	if finish_run:
		file=open(dest+"/completed","r")
		output=file.read()
		file.close()
		timeout_flag=0
	else:
		file=open(dest+"/output","r")
		output=file.read()
		file.close()
		timeout_flag=1
		
	send_res={"output":output,"error":error,"fail":fail,"timeout":timeout_flag,"id":id_no}
	#shutil.rmtree("./temp/"+folder_name)
	return(jsonify(send_res))

if __name__ == '__main__':
	application.run()
