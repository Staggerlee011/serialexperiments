Title: Kubernetes workstation setup
Date: 2020-12-09
Tags: kubernetes
Category: Blog
Summary: My workstation setup for kubernetes

this is my current setup for kubernetes (running on wsl ubunutu-18)

## install software

i currently use:

- kubectl
- kube-ps1
- kubectx
- octant

all of these can be installed via brew:

``` bash
brew install kubectl kube-ps1 kubectx octant
```

### configure kube-ps1

after installing kube-ps1 you will also need to update `~/.bashrc`

``` bash
sudo vim ~/.bashrc
```

insert into the file **MAKE SURE TO DO THIS AT THE BOTTOM OF THE PAGE!** the code below and save and exit `:wq`

``` bash
source "$(brew --prefix)/opt/kube-ps1/share/kube-ps1.sh"
PS1='$(kube_ps1)'$PS1
```

once youve saved the file re `source` it and it should load up in your terminal

``` bash
source ~/.bashrc
```

## Set up kubectl alias

As someone who cant spell or type, alias's are my friend, i just the common alias of `k = kubectl`

``` bash
sudo vim ~/.bash_aliases
```

insert into the file the below:

``` bash
alias k='kubectl'
```

save the changes `:wq` and exit out

## kubectx renaming

i also then use `kubectx` to rename all eks clusters, otherwise my terminal would be full before i even before writing anything

for example if i had a eks cluster that was in a `developement` vpc i could

``` bash
kubectx                 # select the development eks cluster
kubectl development=.   # updates the cluster to be named "development"
```

## summary

and thats it for the moment, i really like `kube-ps1` for the easy knowledge that im in the right cluster and `kubectx` for the naming and ease to switch context between them. `Octant` ive not used much, but looks a good replacement for the risk / issues of using the `kubernetes dashboard`.
