---
title: "Setup Python virtualenv"
date: "2019-12-06"
description: "Setup python virtualenv for Windows or Ubuntu"
tags: [
    "python",
]
---

Quick note on running python `virtualenv`, its a repetitive task that always seem to forget the steps on :/

## Installation

``` python
python3 -m pip install virtualenv
```

## Create virtual environment (shorthand)

``` python
python3 -m venv env
```

## Create virtual environment (specify version of python)

``` python
python3 -m virtualenv -p python3 venv
```

## Activate environment

Note, as I was switching between windows 10 and WSL Ubuntu I found out you cant create an environment in one and use it in the other!

Windows: `.\env\Scripts\activate.ps1`

Ubuntu: `source env/bin/activate`

## Exit environment

Windows: `deactivate`

Ubuntu: `source deactivate`
