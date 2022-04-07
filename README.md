git clone git@gitlab.com:Henry.zh/titanic-api.git

cd ./titanic-api

this script was created for CentOS 7, and Minikube.

1, to start the environment, lauch the start.sh script.
before run, chmod a+x filename

for kubernetes,  use 1.kubectl-start.sh
for minikube, use 1.minikube-start.sh

2, to stop, run the cleanup.sh script.

for kubernetes,  use 2.kubectl-cleanup.sh
for minikube, use 2.minikube-cleanup.sh



alias k="minikube kubectl --"
