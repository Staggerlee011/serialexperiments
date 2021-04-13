---
title: "Kubernetes Workstation Setup"
date: "2020-12-14"
summary: "My workstation setup for kubernetes"
tags: [
    "kubernetes",
    "workstation",
]
---

This is my current setup for kubernetes (running on WSL2 ubunutu-18)

## Install software

I currently use the following software to manage and interact with `k8s`:

### Kubectl

Standard k8s cli

- [Link to Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

### Kube-ps1

Visualizes which k8s cluster you are connected to

- [Link to Kube-ps1](https://github.com/jonmosco/kube-ps1)

### Kubectx

Easily switch between k8s clusters and re-name them!

- [Link to Kubectx](https://github.com/ahmetb/kubectx)
  
### Octant

Web based dashboard that uses port-forwarding to access the k8s cluster

- [Link to Octant](https://github.com/vmware-tanzu/octant)

### KubeSeal

Aka `sealedsecrets`. Used to encrypt secrets on file.

-[sealedsecrets](https://github.com/bitnami-labs/sealed-secrets)

### Kustomize

kubectl comes with a very old version `kustomzise` its well worth sticking on the latest version.

-[kustomize](https://kustomize.io/)

### KubeLinter

Analyses Kubernetes YAML files and Helm charts, and checks them against a variety of best practices, with a focus on production readiness and security.

- [Link to KubeLinter](https://github.com/stackrox/kube-linter)

### bash-completion

So you can get tab completion with `kubernetes`

### Inspektor Gadget

Collection of tools to debug and inspect `kubernetes` applications

- [Link to Inpsecktor Gadget](https://github.com/kinvolk/inspektor-gadget)

### ssm-secret

Allow import/export of `kubernetes` `secrets` to/from AWS `SSM`

- [Link to kubectl-ssm-secret](https://github.com/pr8kerl/kubectl-ssm-secret)

## Install via Brew

All of these can be installed via brew:

``` bash
brew install kubectl kube-ps1 kubectx octant kube-linter kustomize kubeseal bash-completion
```

## Install via Krew

`krew` is a tool that allows you to add plugins to `kubectl`

- [Link to Krew](https://github.com/kubernetes-sigs/krew)
- [Install Krew](https://krew.sigs.k8s.io/docs/user-guide/setup/install/)

**Note run:** `source ~/.bashrc` **to refresh wsl**

``` bash
kubectl krew install gadget
kubectl krew install ssm-secret
```

## Set up kubectl alias and tab completion

As someone who cant spell or type, alias's / tab completion are my friend 

### Alias

I use the common alias of `k = kubectl` to try and lower my command line mistakes

``` bash
sudo vim ~/.bash_aliases
```

Insert into the file the below:

``` bash
alias k='kubectl'
```

Save the changes `:wq` and exit out

### Tab Completion

Not something I'm a big fan off as it seems very and unresponsive. But worth having anyway.

``` bash
source <(kubectl completion bash)
echo 'source <(kubectl completion bash)' >>~/.bashrc
```

## Configure kube-ps1

After installing kube-ps1 you will also need to update `~/.bashrc`

``` bash
sudo vim ~/.bashrc
```

`insert` into the file **MAKE SURE TO DO THIS AT THE BOTTOM OF THE PAGE!** the code below and save and exit `:wq`

``` bash
source "$(brew --prefix)/opt/kube-ps1/share/kube-ps1.sh"
PS1='$(kube_ps1)'$PS1
```

Once you've saved the file re `source` it and it should load up in your terminal

``` bash
source ~/.bashrc
```

## Kubectx renaming

I also then use `kubectx` to rename all my EKS clusters, otherwise my terminal would be full before I even started writing anything!

For example if I had a EKS cluster that was in a `developement` VPC I could

``` bash
kubectx                 # select the development eks cluster
kubectx development=.   # updates the cluster to be named "development"
```

## Summary

and that's it for the moment, I really like `kube-ps1` for the easy knowledge that I'm in the right cluster and `kubectx` for the naming and ease to switch context between them. `Octant` I've not used much, but looks a good replacement for the risk / issues of using the `kubernetes dashboard`.
