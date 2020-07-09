# CompilerDock
## Prerequisites
* Python3.7+
* pipenv
* Docker
## Installation and running
* ```git clone``` the repository and ```cd``` into the cloned repository
* run ```docker build -t compiler:v1 .``` to build the docker container
* run ```pipenv install``` to install the required python packages
* run ```pipenv shell``` to enter the virtual terminal and load the .env file
  * NOTE: Change FLASK_ENV based on dev environment
* ```flask run``` to start the server
  
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


## TODO
* Memory limitations on Docker
* Lighter Dockerfile
* Actions on GitHub
* Combine docker shell script with python
* Use quart and Hypercorn
