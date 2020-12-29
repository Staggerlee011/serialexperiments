---
title: "Deploying Confluence to Kubernetes"
date: "2019-12-23"
description: "Run Confluence on Kuberetes"
tags: [
    "kubernetes",
]
---

After spending some time trying to get different confluence `HELM` charts to work and failing (Im sure it was me not the code!), i gave up and wrote my own manifest files to deploy it. You can find the code in my github repo: [atlassian-docker](https://github.com/Staggerlee011/atlassian-docker/tree/master/kubernetes/confluence).

The deployment gives you:

- A single pod `confluence` deployment
- Offloaded `HTTPS` to a custom URL using a loadbalancer
- `EFS` storage to allow for HA

## Pre-reqs / Notes

My manifests and deployment is specific to running kubernetes on `AWS` and uses EFS storage to allow `HA` via having a `EKS` cluster over 2 AZs.
  
You will need to have the `EFS CSI` or someother variation to allow kubernetes to connect a `PersistentVolume` to `EFS` see below for more details:

`https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html`

## AWS Configuration

- `Kubernetes` deployed (I use EKS)
- Either upload a certificate or generate one for `HTTPS`
- `RDS` Postgres database accessible by the EKS cluster
- `EFS` deployed with connection to the EKS cluster

## Update Kubernetes Manifests

Update the below manifests settings to match your environment.

### deployment.yml

The below values need updating to connect to the database:

- Update `ATL_JDBC_URL` value
- Update `ATL_JDBC_USER` value
- Update `ATL_JDBC_PASSWORD` value

Set the proxy name for your URL (ie `confluence.mysite.com`)

- Update the `ATL_PROXY_NAME` value

### service.yml

Add the ARN for your certificate:

- Update `service.beta.kubernetes.io/aws-load-balancer-ssl-cert` with the cert `ARN`

### storage.yml

Add the EFS id to the `PersistentVolume`

- Update `volumeHandle` with the EFS ID

## Kubernetes Deployment

Once all the manifests have been updated, your ready to deploy.

``` python
kubectl apply -f confluence/namespace
kubectl apply -f confluence
```

And there you have it, with fingers crossed you should now be able to go to your URL and see a confluence setup page :)
