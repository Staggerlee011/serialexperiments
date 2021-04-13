---
title: "Driftctl by Example"
date: "2021-03-05"
summary: "Examples of driftctl"
tags: [
    "driftctl",
    "terraform",
]
---

`driftctl` is a new tool, recently released that reports on drift of your `terraform` code in `AWS`.

Running a scan will output all objects created in a region that are not part of your `terraform` code. We've been using it to find drift of `terraform` code and for rogue manual objects being created.

So far I'm really liking it and expect more functionality to added it evolves. But definitely worth checking it out if you want to add more `testing` around your `IaC`.

## Install

Currently there's no package management options but you can install via

``` bash
curl -L https://github.com/cloudskiff/driftctl/releases/latest/download/driftctl_linux_amd64 -o driftctl
chmod +x driftctl
sudo mv driftctl /usr/local/bin/
```

## Compare against s3 state using a AWS named profile

Run a `driftctl` scan against `ALL` tfstate in a `s3 bucket`

``` bash
AWS_PROFILE=eng driftctl scan \
--from tfstate+s3://<S3 Bucket>/
```

## Run a scan against specific tagged resources

You may want to check for drift against deployed `IaC` which is `tagged`. The below will only show drift for objects with a tag key of `TerraformWorkspace` and value of `core`

``` bash
AWS_PROFILE=<Profile Name> driftctl scan --from tfstate+s3://<S3 Bucket>/core/terraform.tfstate --filter "Attr.Tags.TerraformWorkspace == 'core'"
```

## Ignore objects

There are going to be objects created outside of terraform that you want to ignore, things like your `tfstate` `s3` bucket / `dynamodb` table. Or maybe objects created via the `Serverless Framework` or `SAM` which overlays onto `Cloudformation`

Create a file in the location you are running the scan from named: `.driftignore`

Format is like:

``` yaml
## terraform state managemenet
aws_s3_bucket.engineering-statefile
aws_dynamodb_table.engineering-locks

## ignore ami created via packer
aws_ami:*
```

## Resources

- [driftctl github](https://github.com/cloudskiff/driftctl)
- [driftctl discord server](https://discord.com/invite/NMCBxtD7Nd)
- [driftctl resources lists](https://docs.driftctl.com/0.6.0/providers/aws/resources/)
