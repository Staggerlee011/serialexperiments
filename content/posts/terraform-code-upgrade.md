---
title: "Terraform Code Upgrades"
date: "2023-01-28"
description: "How to upgrade your legacy Terraform code to 0.14"
tags: [
    "terraform",
]
---

We currently have a `terraform` code in multiple versions at present. Below are the basic steps to upgrade code from `0.12` - `0.14`. Note this solution is dependant on using `tfenv` which lets you install multiple versions of `terraform`.

First here's the error you will see:

``` bash
Upgrading to Terraform v0.14 - Terraform by HashiCorpwww.terraform.io › upgrade-guides › 0-14
You will need to successfully complete a terraform apply at least once under Terraform v0. 13

https://www.terraform.io/upgrade-guides/0-14.html
```


remove terrafomr (may have to remove terragrunt as well if you use it)

brew remove terraform

brew install tfenv

tfenv install latest
tfenv install latest:^0.13

find all versions possible to install@ tfenv list-remote
list all versions installed@ tfenv list

get error: 



use specific version of tf

tfenv use
tfenv use latest 

tfenv use 0.13.6

----------------

RUN UPGRADE:

tfenv use 0.13.6

terraform upgrade 0.13upgrade

```
$ terraform 0.13upgrade

This command will update the configuration files in the given directory to use
the new provider source features from Terraform v0.13. It will also highlight
any providers for which the source cannot be detected, and advise how to
proceed.

We recommend using this command in a clean version control work tree, so that
you can easily see the proposed changes as a diff against the latest commit.
If you have uncommited changes already present, we recommend aborting this
command and dealing with them before running this command again.

Would you like to upgrade the module in the current directory?
  Only 'yes' will be accepted to confirm.

  Enter a value: yes

-----------------------------------------------------------------------------

Upgrade complete!

Use your version control system to review the proposed changes, make any
necessary adjustments, and then commit.
```

terraform apply errir:

you need to run terraform init after upgrade!

```
$ terraform apply

Error: Could not load plugin


Plugin reinitialization required. Please run "terraform init".

Plugins are external binaries that Terraform uses to access and manipulate
resources. The configuration provided requires plugins which can't be located,
don't satisfy the version constraints, or are otherwise incompatible.

Terraform automatically discovers provider requirements from your
configuration, including providers used in child modules. To see the
requirements and constraints, run "terraform providers".

2 problems:

- Failed to instantiate provider "registry.terraform.io/hashicorp/aws" to
obtain schema: unknown provider "registry.terraform.io/hashicorp/aws"
- Failed to instantiate provider "registry.terraform.io/-/aws" to obtain
schema: unknown provider "registry.terraform.io/-/aws"
```

terraform init: 

```
$ terraform init
Initializing modules...

Initializing the backend...

Initializing provider plugins...
- Finding hashicorp/aws versions matching "~> 3.7.0, >= 2.23.*, >= 2.23.*, >= 2.50.*, >= 2.50.*"...
- Finding latest version of -/aws...
- Installing hashicorp/aws v3.7.0...
- Installed hashicorp/aws v3.7.0 (signed by HashiCorp)
- Installing -/aws v3.25.0...
- Installed -/aws v3.25.0 (signed by HashiCorp)

The following providers do not have any version constraints in configuration,
so the latest version was installed.

To prevent automatic upgrades to new major versions that may contain breaking
changes, we recommend adding version constraints in a required_providers block
in your configuration, with the constraint strings suggested below.

* -/aws: version = "~> 3.25.0"

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```



versions.tf

``` yml
terraform {
  required_version = ">= 0.14"
}
```


``` bash
$ terraform init
Initializing modules...

Initializing the backend...

Error: Invalid legacy provider address

This configuration or its associated state refers to the unqualified provider
"aws".

You must complete the Terraform 0.13 upgrade process before upgrading to later
versions.
```