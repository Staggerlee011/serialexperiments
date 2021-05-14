---
title: "Inspec AWS RDS best practise benchmark"
date: "2021-05-14"
summary: ""
tags: [
    "inspec",
    "github",
    "aws"
]
---

I've just published a new `github` repo that contains a collection of base best practises for your `rds` instances.

## Example usage

Create you `inspec` profile (For help see my blog post: `https://blog.serialexperiments.co.uk/posts/inspec-by-example/`)

Update file `inspec.yml` depends on section with `rds-bp-benchmark`

``` yml
depends:
  - name: inspec-aws
    url: https://github.com/inspec/inspec-aws/archive/master.tar.gz
  - name: rds-bp-benchmark
    git: https://github.com/Staggerlee011/rds-bp-benchmark
    branch: master
```

Add file `controls/include.rb` and edit

``` ruby
include_controls 'rds-bp-benchmark'
```

Add or update `inputs.yml`

``` yml
rds_name: 'my-rds-instance'
region: 'eu-west-2'
rds_engine: 'postgres'
rds_securitygroup: 'rds-sg'
```

Run `inspec`

``` bash
inspec exec . -t aws:// --input-file inputs.yml
```

I've put each test into its own `control` so you can skip them if you wish as well as making most of the controls have editable values.
Again you can see more of how to do that in the in my blog post `inspec by example`.

I'm hoping this helps you and others. please feel free to offer updates.
