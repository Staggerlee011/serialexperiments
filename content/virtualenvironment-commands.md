Title: Quick setup of python virtualenvironment
Date: 2020-12-07
Tags: runbook,python, ubuntu, windows
Category: Runbook
Summary: Setup python virtualenvironment for windows or ubuntu

Quick note on running python virtual environment, its a repeative task that always seem to forget the steps on :/ 

## installation

``` python
python3 -m pip install virtualenv
```

## create virtual environment

``` python
python3 -m venv env
```

## activate environment

note, as i was switching between windows 10 and wsl ubuntu i found out you cant create an environment in one and use it in the other!

Windows: `.\env\Scripts\activate.ps1`

Ubuntu: `source env/bin/activate`

## exit environment

Windows: `deactivate`

Ubuntu: `source deactivate`
