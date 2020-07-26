# CompilerDock
CompilerDock is a Docker based sandbox code compiler. It currently supports 10 of the most popular languages with more to be added in the future. The code compiler can be easily used to allow users to compile and run the code right on the browser. CompilerDock runs programs in complete isolation, this prevents untrusted code from damaging the remote system executing the program. It can be deployed and run as an API service on any remote or local machine. The API is asynchronous and scalable. Code Judge functionality will also be added in the near future. 
## How does it work?
Client side webapp submits the code and the language it was written in, along with optional inputs. The API then creates a new Docker container, compiles and runs the piece of code inside the container in complete isolation. Once the output/error is generated, it returns this back to the client side webapp and destroys the container. This prevents any damage to the API host as well as prevents multiple user programs from influencing each other as each piece of code runs in it's own container. Example API calls are described below. Checkout [API.md](https://github.com/amanmalali/CompilerDock/blob/mridul303-patch-1/API.md) for the API documentation.

Demo Application: [compilerDock]http://compilerdock.surge.sh/

## Prerequisites
* Python3.7+
* pipenv
* Docker
## Installation and running
* ```$git clone``` the repository and ```$cd``` into the cloned repository
* run ```$docker build -t compiler:v1 .``` to build the docker container
* run ```$pipenv install``` to install the required python packages
* run ```$pipenv shell``` to enter the virtual terminal and load the .env file
  * NOTE: Change QUART_ENV based on dev environment ```$export QUART_APP=application:app```
* ```$quart run``` to start the server

## Demo Application
* Demo web application code presides inside the ```demo``` folder.
* Steps to run the web application:
  * Make sure ```node``` and ```Angular-cli``` is installed.
  * Navigate to ```/demo/compilerdock```.
  * Run ```npm install```
  * Run ```npm start``` and the app will be served at ```localhost:4200```.
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

## Testing
The project uses tox and pytest for testing
Run ```tox``` to start the testing. 
If you contribute to the project, please make sure to add/modify test cases.


## TODO
* Memory limitations on Docker
* Lighter Dockerfile
* Actions on GitHub
* Combine docker shell script with python
* ~~Use quart and Hypercorn~~
