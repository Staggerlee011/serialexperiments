Title: port-forwarding pgadmin
Date: 2020-12-03
Tags: kubernetes
Category: Runbook
Summary: run for kubernetes port-forwarding pgadmin

## Issue

Youve deployed a RDS instances for your EKS/kubernetes cluster into a private subnet and dont have a bastion up to run pgadmin on.

You want to connect to a postgres database quickly

## Solution

Bring up a pod with pgadmin (if your running a private EKS you need to use a private ECR)

``` c#
kubectl run pgadmin --image dpage/pgadmin4 --env="PGADMIN_DEFAULT_EMAIL=admin@admin.com" --env="PGADMIN_DEFAULT_PASSWORD=logmein"
```

port-forward into pgadmin

``` c#
kubectl port-forward pgadmin 8080:80
```

Delete pod till needed again

``` c#
kubectl delete pod pgadmin
```
