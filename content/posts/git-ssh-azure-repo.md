---
title: "Connect to Azure-Repo via SSH"
date: "2021-03-11"
summary: "Steps to connect to a Azure-Repo via SSH"
tags: [
    "azure-repo",
    "azure-devops",
    "git",
]
---

Below are step by step instructions for setting up `SSH` access to an `azure-repo`

## Create SSH key

First create a key via `ssh-keygen`

``` bash
cd ~/.ssh
ssh-keygen -f azure-repo -t rsa -b 4096
```

You will be asked for `passphrase` I've had issues with using one with `VSCode` / `Remote WSL` so suggest not using one.

A typical output will look like below:

``` bash
$ ssh-keygen -f azure-repo -t rsa -b 4096
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in azure-repo.
Your public key has been saved in azure-repo.pub.
The key fingerprint is:
SHA256:1nDTaZZ7vUjfYjxcSwW+OEEpCGUrhcJ8HgShPd+iv+Y stephen@navi
The key's randomart image is:
+---[RSA 4096]----+
|   oo+o++.  ...  |
|   o+ +o...o.+ . |
|  . o+..o o.B . .|
|     o.o + + + o.|
|      o S . +.o.o|
|     . o    .=+.+|
|    .        .*+.|
|     ..      . o |
|     oE.         |
+----[SHA256]-----+
```

## Configure SSH

Next you need to configure SSH via the `~/.ssh/config`, to use the new `ssh key` for all your repos. If the file doesn't exist, create it via `touch ~/.ssh/config`. You will need create / update it, with the below:

``` yaml
Host ssh.dev.azure.com
  IdentityFile ~/.ssh/azure-devops
  IdentitiesOnly yes
```

## Azure Devops Configuration

Now log into your `Azure-Devop` account and open `SSH public keys` via:

``` bash
User Settings icon -> SSH public keys
```

![ssh public keys](/azure-repo-ssh/azure-repo-ssh-01.png)

Select `New Key`

![New Key](/azure-repo-ssh/azure-repo-ssh-03.png)

Copy and Paste your new public `ssh` key into the web portal of `Azure-Devops`:

``` bash
cat ~/.ssh/azure-repo.pub
```

![Add Key](/azure-repo-ssh/azure-repo-ssh-02.png)

## Test SSH

Now  test your connection:

``` bash
ssh -T git@ssh.dev.azure.com
```

This should output below:

``` bash
remote: Shell access is not supported.
shell request failed on channel 0
```

If you don't get this message, check your config or look at the resources section below for more troubleshooting steps.

## Connect to Azure-Repo

Your now ready to connect to all repos in the `azure-devops` organization (Unless RBAC has been implemented) via your normal `git clone`, First get the `URL` for `ssh` from the repo:

![Add Key](/azure-repo-ssh/azure-repo-ssh-04.png)

Then run the clone command

``` bash
$ git clone git@ssh.dev.azure.com:v3/<YOUR ORG>/<PROJECT>/<REPO>
Cloning into '<REPO>'...
remote: Azure Repos
remote: Found 69 objects to send. (96 ms)
Receiving objects: 100% (69/69), 21.50 KiB | 1.02 MiB/s, done.
```

## Resources

- [Azure-Repo Questions and Troubleshooting](https://docs.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops#questions-and-troubleshooting)
