# CompilerDock
## Prerequisites
* Python3
* Docker
  * Docker can also be installed using the included install script
## Installation
* Run install.sh script in the Setup directory as root user. Install will take about 20 minutes
  * ```$sudo ./install.sh ```
* The script will install ```docker-ce```, ```pip3```, ```gunicorn``` and enables Docker commands to be run without ```$sudo```
* Verify installation by running ```$docker version```
* Install Python packages by using requirements.txt in the Setup folder 
  * ```$sudo pip3 install -r requirements.txt```
* Test the API by running the flask server ```$python application.py```
* If the terminal says ```* Running on http://127.0.0.1:5000/``` The installation is successful

## Current languages supported 
* C
* C++
* Python3
* Java
* JavaScript (NodeJS)
* GO
* R
* PHP
* Ruby
* Rust

Additional languages will be added over time, they can be requested by raising an issue as a feature request
Some languages may cause errors in certain situations, please raise an issue with the code run and the language

## Selecting languages to install
Additional languages can be added by adding the appropriate command in the Dockerfile located in the Setup folder
* ``` RUN apt-get install <Name of ubuntu package for the language>```
Languages can also be removed from the dockerfile if they are not needed by deleting the corresponding RUN command in the Dockerfile
