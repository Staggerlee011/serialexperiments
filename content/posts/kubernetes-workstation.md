---
title: "Kubernetes Workstation Setup"
date: "2020-12-14"
description: "My workstation setup for kubernetes"
tags: [
    "kubernetes",
]
---

This is my current setup for kubernetes (running on wsl ubunutu-18)

## Install software

I currently use:

### kubectl

Standard k8s cli

### kube-ps1

Visualizes which k8s cluster you are connected to

### kubectx

Easily switch between k8s clusters and re-name them!

### octant

Web based dashboard that uses port-forwarding to access the k8s cluster

### Install via Brew

All of these can be installed via brew:

``` bash
brew install kubectl kube-ps1 kubectx octant

```
## Set up kubectl alias

As someone who cant spell or type, alias's are my friend, I use the common alias of `k = kubectl` to try and lower my command line mistakes

``` bash
sudo vim ~/.bash_aliases
```

Insert into the file the below:

``` bash
alias k='kubectl'
```

Save the changes `:wq` and exit out

### Configure kube-ps1

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
kubectl development=.   # updates the cluster to be named "development"
```

## Summary

and that's it for the moment, I really like `kube-ps1` for the easy knowledge that I'm in the right cluster and `kubectx` for the naming and ease to switch context between them. `Octant` I've not used much, but looks a good replacement for the risk / issues of using the `kubernetes dashboard`.
