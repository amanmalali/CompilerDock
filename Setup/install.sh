apt update
apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
apt update
apt-cache policy docker-ce
apt install -y docker-ce
apt install -y gunicorn
apt install python3-pip
usermod -aG docker ${USER}
chmod 666 /var/run/docker.sock
docker build -t "compiler:v1" - < Dockerfile
pip3 install -r `pwd`/requirements.txt
#gunicorn -w 10 --bind 0.0.0.0:80 application:application
# sudo su - ${USER}  Run this command in terminal after all of this
