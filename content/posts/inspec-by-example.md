---
title: "Inspec by Example"
date: "2021-05-12"
summary: "Example commands for Inspec"
tags: [
    "inspec"
]
---

Collection of examples and commands to run, manage and develop with `inspec`:

<!-- TOC -->

- [Installation](#installation)
  - [Install plugin pre-steps](#install-plugin-pre-steps)
  - [Install plugin](#install-plugin)
- [Using Inspec](#using-inspec)
  - [Create a new profile](#create-a-new-profile)
  - [Execute a profile](#execute-a-profile)
    - [Execute profile with Input values](#execute-profile-with-input-values)
- [Development with Inspec](#development-with-inspec)
  - [Inspec.lock](#inspeclock)
  - [Depends_on](#depends_on)
    - [depends_on github](#depends_on-github)
    - [depends_on git](#depends_on-git)
    - [depends_on local](#depends_on-local)
  - [Managing dependency tests](#managing-dependency-tests)
    - [Skipping controls](#skipping-controls)
      - [Skip specific control](#skip-specific-control)
      - [Run specific dependency control](#run-specific-dependency-control)
    - [Edit dependency controls](#edit-dependency-controls)
  - [Libraries](#libraries)
- [Resources](#resources)

<!-- /TOC -->

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

You may wish to add a plugin, that can be done via:

``` yaml
sudo gem install train-kubernetes

```

## Using Inspec
### Create a new profile

You can create a new profile and base it on some pre-created profiles, the below creates a `inspec-aws` based basic profile:

``` yaml
inspec init profile --platform aws my-profile
```

### Execute a profile

To run a profile you use the `exec` command. The below is an example of running a test against an `aws://`  resource:

``` yaml
inspec exec . -t aws://
inspec exec . -t aws://<aws profile name>
```

#### Execute profile with Input values

``` yaml
inspec exec . -t aws:// --input-file inputs.yml
inspec exec . -t aws:// --input rds_name=myrdsinstance
```

## Development with Inspec

Collection of examples for editing and developing `inspec` profiles.

### Inspec.lock

This file locks your `inspec.yml` so all future runs are the same. This means that any dependency changes or config
changes to `inspec.yml` will not made if you keep the `inspec.lock`. To run updated tests you will need to delete the file.

### Depends_on

You may want to build your profile on other profiles. Using this kind of modulation lets you re-use your tests in different environments.

#### depends_on github

Example shows how you load up the `inspec-aws` profile

```yaml
depends:
  - name: inspec-aws
    url: https://github.com/inspec/inspec-aws/archive/master.tar.gz
```

#### depends_on git

Example using `git` which gives a good version lock in via using branches/tag

```yaml
depends:
- name: git-profile
  git: http://url/to/repo
  branch:  desired_branch
  tag:     desired_version
  commit:  pinned_commit
  version: semver_via_tags
  relative_path: relative/optional/path/to/profile
```

#### depends_on local

Example shows how you load up a file from local storage:

```yaml
depends:
  - name: profile
    path: ../path/to/profile
```

### Managing dependency tests

When you pull in a set of tests, you need to reference the tests to have them running.
I do this via adding a new file under controls called `include.rb` which a reference to each
profile you want to add:

``` ruby
include_controls 'rds-bp-benchmark'
```

#### Skipping controls

You may want to ignore some controls. this can be done in 2 ways:

##### Skip specific control

via updating the `include.rb`

``` ruby
include_controls 'rds-bp-benchmark' do
  skip_control 'snapshot tags'
end
```

##### Run specific dependency control

Alternatively you can only run specific controls you want from the dependency via:

``` ruby
require_controls 'rds-bp-benchmark' do
  control 'snapshot tags'
end
```

#### Edit dependency controls

You can also edit a dependency controls on the fly changing values via:

``` ruby
require_controls 'rds-bp-benchmark' do
  control 'snapshot tags' do
    impact 0.1
  end
end
```

### Libraries

This allows you to add `ruby` based code to your profile.

For examples see: `https://github.com/Staggerlee011/rds-bp-benchmark/blob/master/libraries/rds_helper.rb`

## Resources

- [Inspec Glossary](https://docs.chef.io/inspec/glossary/)
- [Inspec Profile inheritance](https://blog.chef.io/understanding-inspec-profile-inheritance)
