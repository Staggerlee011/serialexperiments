---
title: "Kube-linter by Example"
date: "2021-01-21"
summary: "Example usage and possible fixes to kube-linter"
tags: [
    "kubernetes",
]
---

Collection of examples to run and support `kube-linter` suggestions to `kubernetes` manifests

## install

You can install `kube-linter` with `brew`

``` bash
brew install kube-linter
```

## Run against single or multiple manifests

To run `kube-linter`

``` bash
kube-linter lint .
```

## Possible fixes to kube-linter

Below are warnings you could get from `kube-linter` and example solutions to them.

### container "xxx" does not have a read-only root file system

``` yml
apiVersion: v1  
kind: Pod  
metadata:  
  name: xxx 
spec:  
  containers:  
  # specification of the pod’s containers  
  # ...  
  securityContext:  
    readOnlyRootFilesystem: true 
```

### container "xx" is not set to runAsNonRoot

``` yml
apiVersion: v1  
kind: Pod  
metadata:  
  name: xxx  
spec:  
  containers:  
  # specification of the pod’s containers  
  # ...  
  securityContext:  
    runAsNonRoot: true
```
