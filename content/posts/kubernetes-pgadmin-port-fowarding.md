---
title: "Port-forwarding pgadmin"
date: "2020-12-15"
description: "Kubernetes port-forwarding pgadmin"
tags: [
    "kubernetes",
    "database",
]
---

You've deployed a RDS instances for your EKS/kubernetes cluster into a private subnet and don't have a bastion up to run pgadmin on.

You want to connect to a postgres database quickly

## Solution

Bring up a pod with pgadmin (if your running a private EKS you need to use a private ECR for the `--image` value)

``` c#
kubectl run pgadmin --image dpage/pgadmin4 --env="PGADMIN_DEFAULT_EMAIL=admin@admin.com" --env="PGADMIN_DEFAULT_PASSWORD=logmein"
```

port-forward into pgadmin

``` c#
kubectl port-forward pgadmin 8080:80
```

Open your favourite web browser and go to `http://localhost:8080`

And there it is you can now enjoy the joys the pgadmin to connect to your private database server without the need of jump boxes, or external load balancers etc. All locked down to only those than can connect to to your cluster via `kubectl`

## Clean up

Delete pod till needed again

``` c#
kubectl delete pod pgadmin
```
