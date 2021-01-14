---
title: "aws-cli Configure by Example"
date: "2021-01-04"
description: "Basic usage aws-cli for account management"
tags: [
    "aws",
]
---

Another blog post on something super simple that I always forgot the syntax for. Note that `aws-cli` has to be `v2` for some of these commands.

## Named profiles

Create a named profile:

``` bash
aws configure --profile <new profile name>
```

## List named profiles

List all AWS profiles you saved:

``` bash
aws configure list-profiles
```
