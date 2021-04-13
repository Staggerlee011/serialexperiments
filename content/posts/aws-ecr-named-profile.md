---
title: "Push Images to ECR via AWS Named Profile"
date: "2021-01-15"
summary: "Quick example of using the profile switches for macOS/Linux and Windows"
tags: [
    "ecr",
    "aws",
]
---

If you run your AWS environment via multiple accounts. Then you will properly end up with multiple `AWS Named Profiles` to manage access to each `account`. When `pushing` a new image to a ECR repo, a standard quick cheat, is to use the `View Push Commands` button which is on the `AWS Console` as it describes the steps to deploy. The issue with this is that using a `named profile` means adding an extra switch in, sadly this different for `powershell` and `linux` (And i always forget what it is!) Below answers that

## macOS/Linux

Linux uses the `-profile` switch

``` bash
aws ecr get-login-password --region eu-west-2 --profile <my-profile> | docker login --username AWS --password-stdin xxx.dkr.ecr.eu-west-2.amazonaws.com
```

## PowerShell

PowerShell uses the `-ProfileName` switch

``` powershell
(Get-ECRLoginCommand -Region eu-west-2 -ProfileName <my-profile>).Password |docker login --username AWS --password-stdin xxx.dkr.ecr.eu-west-2.amazonaws.com
```