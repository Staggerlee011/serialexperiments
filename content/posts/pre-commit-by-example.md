---
title: "Pre-Commit by Example"
date: "2021-03-02"
summary: "Example Setup and config for NPM"
tags: [
    "git",
    "pre-commit",
]
---

Pre-commit is an easy to use tool that allows you to add in `git hooks` for your repos. This means that every time you run a `commit` command `pre-commit` will run what ever apps you've told it to. This is great for things like `linting` and `formatting`.

## install

There's a couple of ways to install `pre-commit` but I use `brew`

``` bash
brew install pre-commit
```

## pre-commit-config.yaml

For pre-commit to run, you need to add a `pre-commit-config.yaml` file to the `root` of your `git` repo. Below is a common example I use of loading `markdownlinter`, `detect-secrets` and `terraform fmt` (Note these are from different `pre-commit repos` you can stack as many as you like!)

``` yaml
repos:
- repo: git://github.com/antonbabenko/pre-commit-terraform
  rev: v1.47.0 # Get the latest from: https://github.com/antonbabenko/pre-commit-terraform/releases
  hooks:
    - id: terraform_fmt

- repo: https://github.com/Yelp/detect-secrets
  rev: v1.0.1
  hooks:
    - id: detect-secrets
      args: ['--baseline', '.secrets.baseline']
      exclude: package.lock.json
  
- repo: https://github.com/igorshubovych/markdownlint-cli
  rev: v0.26.0
  hooks:
  - id: markdownlint
```

## init

To connect your `pre-commit` file to a repo you need to run `install` in the `root` of the `repo`

``` yaml
pre-commit install 
```

## commands

Collection of common commands

### run all hooks against all files

This will run all your hooks against all files in the repo

``` yaml
pre-commit run -a
```

### run specific hook against all files

- Note that `terraform_ftm` is the `id` of a hook you wish to run

``` yaml
pre-commit run terraform_fmt -a
```

## Resources

- [pre-commit website](https://pre-commit.com/)
  