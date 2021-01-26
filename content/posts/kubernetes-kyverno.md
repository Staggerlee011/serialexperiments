---
title: "Kubernetes Policy as Code with Kyverno"
date: "2020-12-15"
description: "Examples and usage of Kyverno on kubernetes"
tags: [
    "kubernetes",
]
---

With `PSP` being deprecated in `1.21` and fully removed in `1.25` (See the [github conversation here](https://github.com/kubernetes/kubernetes/pull/97171)) its time to start looking around at other options. At present that really sits with [OPA](https://www.openpolicyagent.org/) which means learning a new code/syntax which doesn't seem to friendly to me, or [Kyverno](https://kyverno.io/) which uses a native `kubernetes` manifests to let you deal with your policy management. For me, as we don't have to many policies at the moment, `kyverno` fits our needs better. below is basic syntax and usage examples.

## Install

You can install via `manifest` or `HELM`, we use `kustomize` so download the `install.yml` file and use that as a base then overlay our `ecr` images

``` bash
kubectl create -f https://raw.githubusercontent.com/kyverno/kyverno/main/definitions/release/install.yaml
```

Basic overlay example

``` yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
- ../../base

images:
- name: ghcr.io/kyverno/kyverno
  newName: dkr.ecr.eu-west-2.amazonaws.com/kyverno
  newTag: v1.3.2-rc1

- name: ghcr.io/kyverno/kyvernopre
  newName: dkr.ecr.eu-west-2.amazonaws.com/kyvernopre
  newTag: v1.3.2-rc1
```

## Reading Policies

Policies are split between `namespace` and `cluster`

### Namespace

``` bash
kubectl get policyreport -A
```

### Cluster

``` bash
kubectl get clusterpolicyreport -A
```

#### View Violations

``` bash
kubectl describe polr -A | grep -i "status: \+fail" -B10
```

or specific to namespace

``` bash
kubectl describe polr polr-ns-default | grep "Status: \+fail" -B10
```

## Delete all policies

``` bash

```

Example policy to audit the use of the label `app: "?*"`

``` yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: audit-app-label
spec:
  validationFailureAction: audit
  rules:
  - name: check-for-app-labels
    match:
      resources:
        kinds:
        - Pod
    validate:
      message: "The label `app` is required."
      pattern:
        metadata:
          labels:
            app: "?*"
```
