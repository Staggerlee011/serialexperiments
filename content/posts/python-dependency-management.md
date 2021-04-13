---
title: "Python Dependency Management"
date: "2020-12-29"
summary: "Basic python dependency management steps"
tags: [
    "python",
]
---

Below are some basic python dependency management steps. that can be used to control your python work.

## New Project

If your starting a new python script/function/module/package you'll properly want to create one or many virtual environments I like virtualenv ([read my post here about setting this up](https://blog.serialexperiments.co.uk/posts/setup-virtualenvironment))

### Install dependencies

Next you'll want to install some modules/packages to support your work

``` python
python3 -m pip install x y z
```

## Save dependencies

After installing we will want to save them to a `requirements.txt` for future builds / setups

``` python
python3 -m pip freeze > requirements.txt
```

## Load dependencies from requirements

If you have a `requirements.txt` file you can then load all dependencies in a single command via

``` python
python3 -m pip install -r requirements.txt
```
