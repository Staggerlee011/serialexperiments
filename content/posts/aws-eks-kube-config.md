---
title: "EKS Kube Config"
date: "2021-01-15"
summary: "Code for connecting to a new EKS Cluster"
tags: [
    "kubernetes",
    "aws",
    "eks"
]
---

To run kubectl commands against an a `EKS` cluster you must first authenticate with it. `kubectl` manages credentials via the `~/.kube/config` file. To get your credentials for a new `eks` cluster you will need to use the below  `aws-cli` command.

## Pre-Req

- kubectl installed
- aws named profile set up for the account
- IAM permissions to access the EKS cluster

## Command

``` bash
aws eks --region eu-west-2 update-kubeconfig --name <EKS-CLUSTERNAME> --profile <AWS-PROFILE-NAME>
```
