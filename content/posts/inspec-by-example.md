---
title: "Inspec by Example"
date: "2021-12-17"
summary: "Example commands for Inspec"
tags: [
    "inspec"
]
---

## Installation

Install `inspec`

``` yaml
brew install ruby # you have ruby installed but unless you specifically need an older version upgrade?
gem install inspec
```


### Install plugin pre-steps

Inspec is built around plugin extensions. I had to install a few extra bits first to get extensions installing

``` yaml
sudo gem install chef-utils -v 16.6.14
```

### Install plugin

``` yaml
sudo gem install train-kubernetes
```

## aws tests

init the tests with the below to get a basic profile

``` yaml
inspec init profile --platform aws my-profile
```

run inspec tests via:

``` yaml
inspec exec . -t aws://<aws profile name>
```

## kubernetes tests

``` yaml
inspec exec . -t aws://<aws profile name>
```