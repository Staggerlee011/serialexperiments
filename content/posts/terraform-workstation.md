---
title: "Terraform Workstation Setup"
date: "2022-01-28"
description: "My workstation setup for Terraform"
tags: [
    "terraform",
    "workstation",
]
---

This is my current setup for `terraform` (running on WSL2 ubunutu-18)

## Install software

I currently use the following software to manage and interact with `terraform`:

### tfenv

Terraform releases are quick and keeping all our environments on the same version isn't possible. `tfenv` resolves that by letting us have multiple versions installed and easy to manage.

### tfsec



## tfenv configuration

We currently have code in 12/13 and 14. We upgrade any `terraform` that is edited or when we have time in a sprint to refactor. With that I get the latest `terraform` 14 and 13.

``` bash
tfenv install latest
tfenv install latest:^0.13
tfenv use latest
```

### tfenv basic syntax

- List all versions of `terraform` available: `tfenv list-remote`
- List installed versions of `terraform` `tf list` (This also shows the current version in use)
- Define `terraform` version to use `tfenv use latest` or `tfenv use 0.13.6`

### tfenv support

If you run `tfenv list` and get the below error. This is because you have not set which version of `terraform` to use. once defined error goes away ie: `tfenv use latest`

``` bash
$ tfenv list
cat: /home/linuxbrew/.linuxbrew/Cellar/tfenv/2.0.0/version: No such file or directory
Version could not be resolved (set by /home/linuxbrew/.linuxbrew/Cellar/tfenv/2.0.0/version or tfenv use <version>)
```
