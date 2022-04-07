minikube kubectl -- delete service flask 
minikube kubectl -- delete deployment flask
minikube kubectl -- delete service postgres 
minikube kubectl -- delete deployment postgres
minikube kubectl -- delete persistentvolumeclaim postgres-pv-claim
minikube kubectl -- delete persistentvolume postgres-pv-volume
minikube kubectl -- delete secret postgres-secrets