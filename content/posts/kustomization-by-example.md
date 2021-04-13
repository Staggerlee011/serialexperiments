---
title: "Kubectl Kustomization by Example"
date: "2021-01-10"
summary: "Example syntax for Kustomization files using kubectl"
tags: [
    "kubernetes",
]
---

NOTE: This guide is for using `kustomize` in `kubectl` which uses a old version of `kustomize` this means your writing a lot of `deprecated` codes like using `bases`. 

`Kustomize` is a standalone tool to customize Kubernetes objects through a `kustomization` file. It has been part of `kubectl` since `v1.14` These examples are based on using the built in version of `kubectl` but it is strongly suggested to migrate away and use the latest version.

## Run kustomization file

To `apply` or `delete` a set of `manifests` you use the `-k` command

``` bash
kubectl apply -k k8s/my-app/overlays/production/
```

## View generated output of kustomization

To view the `manifest` that gets generated from `kustomize` you can the below command pointing at the the `base` or `overlays/env` folder

``` bash
kubectl kustomize k8s/my-app/overlays/production/
```

## base settings

Below are examples of the `base` `kustomization` file

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

Below are examples of overlays for various manifests and options.

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
- name: nginx # note this is the image: tag not the name of the container
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
