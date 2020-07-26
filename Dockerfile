FROM ubuntu:latest
RUN mkdir /scripts
COPY ./src/scripts/run.sh /scripts
RUN apt-get update
RUN apt-get install -y curl gcc g++ software-properties-common python3 default-jre default-jdk golang r-base php-cli ruby-full npm --no-install-recommends
# RUN apt-get install -y gcc
# RUN apt-get install -y g++
# RUN apt-get install -y software-properties-common
# RUN apt-get install -y python3
# RUN apt-get install -y default-jre
# RUN apt-get install -y default-jdk
# RUN apt-get install -y golang
# RUN apt-get install -y r-base
# RUN apt-get install -y php-cli
# RUN apt-get install -y ruby-full
# RUN apt-get install -y npm
RUN npm install -g underscore shelljs sys lodash async body-parser
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
