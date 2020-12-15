---
title: "setup of python virtualenvironment"
date: "2019-12-06"
description: "Setup python virtualenvironment for windows or ubuntu"
tags: [
    "python",
]
---

Quick note on running python virtual environment, its a repeative task that always seem to forget the steps on :/ 

## installation

``` python
python3 -m pip install virtualenv
```

## create virtual environment (shorthand)

``` python
python3 -m venv env
```

## create virtual enivronment (specify version of python)

``` python
python3 -m virtualenv -p python3 venv
```

## activate environment

note, as i was switching between windows 10 and wsl ubuntu i found out you cant create an environment in one and use it in the other!

Windows: `.\env\Scripts\activate.ps1`

Ubuntu: `source env/bin/activate`

## exit environment

Windows: `deactivate`

Ubuntu: `source deactivate`
