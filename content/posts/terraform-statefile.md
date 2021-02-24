---
title: "Terraform Remote Statefile Creation"
date: "2020-12-07"
summary: "Terraform code to generate a secure S3 bucket for remote state"
tags: [
    "terraform",
]
---

When you deploy Terraform you'll want to have a remote state setup to manage team access. For AWS the standard is to use S3 bucket. As you cant store the state of bucket IN the bucket, its one of the only things that you have to leave outside of being controlled via the remote state.

For our teams we manage this via still creating the s3 bucket in Terraform and keep the code in source control, this is normally stored in a `.state` folder along with the other workspaces.

``` c#
- terraform
  - .state
  - core
  - eks
  - rds
```

The below is a gist example of the code we use, id suggest also adding a `version.tf` in the folder that matches the rest of your workspaces.

{{< gist Staggerlee011 b08b80dad659cd549030e5855a798673 "terraform-statefile-bucket.tf" >}}
