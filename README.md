# CompilerDock
## Installation
* Run install.sh script in the Setup directory as root user
  * ```$sudo ./install.sh ```
* The script will install ```docker-ce```, ```pip3```, ```gunicorn``` and enables Docker commands to be run without ```$sudo```
* Verify installation by running ```$docker version```
* Install Python packages by using requirements.txt in the Setup folder 
  * ```$sudo pip3 install -r requirements.txt```
* Test the API by running the flask server ```$python application.py```
* If the terminal says ```* Running on http://127.0.0.1:5000/``` The installation is successful
