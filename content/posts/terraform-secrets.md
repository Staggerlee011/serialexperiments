---
title: "Terraform secrets using SSM and KSM"
date: "2021-04-12"
summary: "How to safely store secrets in your terraform source control using AWS SSM / KMS"
tags: [
    "terraform",
    "secrets",
    "aws-kms",
    "aws-ssm",
]
---

You never want to keep your secrets in plaintext and you never want to keep your plaintext secrets in source control!

With `terraform` a lot of the time you are creating objects and you can use the `random` resource to generate a secret and either push to `output` or to a secure service to store it (We use `parameter store`/`ssm`).

But in some cases you may have to add a secret into terraform that has already been created and there comes the problem! below is a possible solution for `AWS` using `aws-kms` and `ssm`.



## Pre-reqs

- A `aws-kms` to connect to and generate your `secrets` from
- `aws-cli` installed (`> v2` in the below examples)

## Generate plaintext file

Create a `temporary text` file, this will contain your `secret` in plaintext and uses `key` : `value` pairing. 

    `We will delete after generating our secret file!`

### Example file

An example file would be:

``` yaml
password: examplepassword
```

## Generate secret file

Run the below command, updating the following:

- `profile` = `aws named profile` or remove line if you use `default`
- `key-id` = the `key-id` of your `kms`, you can get this from the `console` or output from `terraform`
- `region` = the region your `kms` is stored in
- `plaintext` = the location of the file with the `plaintext secret`

``` bash
aws kms encrypt \
  --profile mgmt-eks \
  --key-id 346e8eab-39a6-455b-ac88-fcd8a6cf7043 \
  --region eu-west-2 \
  --plaintext fileb://user.yml \
  --output text \
  --query CiphertextBlob
```

This will generate the `secret`, copy the output to a file named: `password.yml.encrypted` and save it (I put my secrets in a folder with the same name as the `tf` file)

    Delete the `plaintext` secret!

## Update TF

Now we have a `secret` that can be saved to `source control`. Add a `data source` pointing to the file

``` yaml
data "aws_kms_secrets" "myapp" {
  secret {
    name    = "password"
    payload = file("${path.module}/myapp/password.yml.encrypted")
  }
}
```

Add a local call to the decrypted answer. In the below example im just taking the `secret` and saving it to `ssm` this can then be called in `tf` or any other app and never be hardcoded.

``` yaml
locals {
  myapppass = yamldecode(data.aws_kms_secrets.myapp.plaintext["password"])
}

resource "aws_ssm_parameter" "myapp_password" {
  name        = "/myapp/user/admin/password"
  description = "password for admin user"
  type        = "SecureString"
  value       = local.myapppass.password
  tags = {
    "Terraform" = "true"
    "myapp"    = "true"
  }
}
```

There we have it. You are ready to `terraform apply` This will leave your `source control` clean and your secrets safe.

There are other options for how to do keep your secrets safe. But this is the easiest to set up and run with.
