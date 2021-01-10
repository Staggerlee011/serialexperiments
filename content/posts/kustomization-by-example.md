---
title: "kustomization by example"
date: "2019-12-15"
description: "Example syntax for Kustomization files"
tags: [
    "kubernetes",
]
---

`Kustomize` is a standalone tool to customize Kubernetes objects through a `kustomization` file. It has been part of `kubectl` since `v1.14`

## Run kustomization file

``` bash
kubectl apply -k k8s/my-app/overlays/production/
```

## View generated output of kustomization

``` bash
kubectl kustomize k8s/my-app/overlays/production/
```

## base settings

below are examples of the `base` `kustomization` file

### resources

This is the most basic usage of `kustomization`. Allowing you to deploy a `namespace` and other `manifests` at the same time

``` yml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: confluence
resources:
- ./namespace.yml
- ./storage.yml
- ./deployment.yml
- ./service.yml
```

## overlays settings

below are examples of overlays for various manifests and options.

### image or tag

Update the tag of the image pulled via overlay:

``` yml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
- ../../base

images:
- name: nginx
  newTag: 1.19
```

You could also update the image as well via if you say need to use a different `repository`

``` yml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
- ../../base

images:
- name: nginx
  newName: <NEW ECR PATH>/nginx
  newTag: 3.4.5
```

### patchesStrategicMerge

If you need to update a value of a `manifest` file from the base, the easist way is to create a new file in the `overlays/env` folder and reference it via `patchesStrategicMerge`.

The file will need to `re-create` the `yml` down to the `value` you are `overwriting` for example:

#### deployment example

A common issue will be updating the `env` variables for the `pods` in a `deplyment` for each `overlay` this can be done via creating a file (Below could is called: `db-deployment.yml`) containing your `env` settings like:

``` yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: confluence
spec:
  template:
    spec:
      containers:
        - name: app
          env:
          - name: ATL_JDBC_URL
            value: "jdbc:postgresql://my-prod-rds-server:5432/db"
          - name: ATL_JDBC_USER
            value: "postgres"
```

and then add a `patchesStrategicMerge` section to `kustomization.yml` and reference the file `db-deployment.yml`

``` yml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
- ../../base

patchesStrategicMerge:
- db-deployment.yml
```

#### service example

Another example would be updating the `arn` for a certificate in each `overlay`. Again you would simply create a new file in `overlays/env` folder (In this example its called `arn-serivce.yml`)

`arn-service.yml` will copy all `yml` from the `base` `serivce` but ignore all other values that are set so would look like:

``` yml
apiVersion: v1
kind: Service
metadata:
  name: dos
  namespace: dos
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:acm:eu-west-2:xx:certificate/xxx
```

Again you would update `kustomization.yml` in the `overlays/env` to reference the new resource

``` yml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
- ../../base

patchesStrategicMerge:
- arn-service.yml
```

### config-maps

You can either write the `configmap` into the `kustomization` file or keep it in an external file. I prefer the later:

``` yml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
- ../../base

patchesStrategicMerge:
- config-map.yml
```