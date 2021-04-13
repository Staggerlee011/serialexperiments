---
title: "SealedSecrets by Example"
date: "2021-01-22"
summary: "Deployment and usage of sealed secrets"
tags: [
    "kubernetes",
]
---

Secrets in `kubernetes` didn't make sense to me (storing passwords in base64) when they are in a cluster I could understand it being secured by `RBAC` but to get it in there you either don't have it in a manifest making `gitops` harder or you worse you have a password in plain text in your source control (dont do that!).

As we migrate more apps to `kubernetes` I did like the idea of the `krew` plugin [ssm-secret](https://github.com/pr8kerl/kubectl-ssm-secret) that means your passwords in `ssm` and you have a one time process of pushing them into `kubernetes`. But as its breaking away from `gitops` and keeping everything together and `simple` I wanted something else. That's when I found `sealedsecrets`. This lets you keep manifests for your secrets but the passwords are encrypted, they are then decrypted on apply to the `kubernetes` cluster.

## Setup

You need to install the client on workstation

``` bash
brew install kubeseal
```

And deploy the application to `kubernetes`. this can be done via manifest or helm. We use `kustomize` so just downloaded the release (currently `v0.13.1`)

``` bash
kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.13.1/controller.yaml
```

### Kustomize install

We use private `eks` clusters. so cant just download from public container repos. with that we created a simple `kustomize` file for each cluster to pull from `ecr` example below of an `overlay`

``` yml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
- ../../base

images:
- name: quay.io/bitnami/sealed-secrets-controller:v0.13.1
  newName: xxx.dkr.ecr.eu-west-2.amazonaws.com/sealedsecrets
  newTag: v0.13.1
```

With an even more simple base:

``` yml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- ./controller.yml
```

## Backup private key

To create a backup of the private key used by `sealedsecrets` run:

``` bash
kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml >master.key
```

    NOTE: THIS KEY SHOULD NOT BE STORED IN SOURCE CONTROL!

## Restore private key

To restore apply the master key and delete the controller pod

``` bash
kubectl apply -f master.key
kubectl delete pod -n kube-system -l name=sealed-secrets-controller
```

## Create Secret using SealedSecret

The only difference between creating a `kubernetes` `secret` and a `sealed secret` is that you pipe the file / command to `kubeseal` and have that output the file.

For `secret` examples please see my post: [Kubernetes Secrets by Example](https://blog.serialexperiments.co.uk/posts/kubenetes-secrets-by-example/)

### format

Like all manifests you can either format to `json` or `yaml`. I prefer `yaml` so use

``` bash
kubeseal --format yaml | tee name-of-manifest-file-to-store-in-source-control.yml
```

leaving kubeseal without the `--format` switch will output to `json`

### example --from-literal

This will create a new `manifest` called `wordpress-user-password-secure.yml` which can be kept with the other manifests for your application as the password is now encrypted.

``` bash
k create secret generic wordpress-user-password --dry-run=client --from-literal password=MySuperSecretPassword --output yaml | kubeseal --format yaml | tee wordpress-user-password-secure.yml
```

## Notes on sealedsecrets

- You must be connected to the cluster you wish to deploy to with `kubectl` when running `kubeseal`
- You cant update the `sealedsecret` after its created and deploy it. It wont work! (This is a good thing)
- You cant deploy the same secret to different namespaces. It wont work! (This is also a good thing)
  
## Resources

- [GitHub Repo for Sealed-Secrets](https://github.com/bitnami-labs/sealed-secrets)
- [The DevOps Toolkit Series - Bitnami Sealed Secrets - How To Store Kubernetes Secrets In Git Repositories](https://www.youtube.com/watch?v=xd2QoV6GJlc&t=21s)
- [Kubernetes Secrets by Example](https://blog.serialexperiments.co.uk/posts/kubernetes-secrets-by-example/)
