kubectl delete service flask 
kubectl delete deployment flask
kubectl delete service postgres 
kubectl delete deployment postgres
kubectl delete persistentvolumeclaim postgres-pv-claim
kubectl delete persistentvolume postgres-pv-volume
kubectl delete secret postgres-secrets