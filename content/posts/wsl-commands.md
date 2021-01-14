---
title: "WSL Helpful Commands"
date: "2020-12-09"
description: "Set of helpful WSL commands"
tags: [
    "wsl",
]
---

Quick reference commands for dealing with `wsl` in windows10

## list wsl distro

this also returns the version of the distro you are running

``` powershell
wsl -l -v
```

## upgrade distro from wsl1 to wsl2

Get the distro name from `wsl -l -v` in the below example im upgrading ubuntu from wsl1 to 2

``` powershell
wsl --set-version Ubuntu-18.04 2
```

## set new default distro

``` powershell
wsl -s Ubuntu-18.04
```

## restart wls distro

``` powershell
wsl -t Ubuntu-18.04
```

## uninstall single distro

go into windows `apps and features` select the distro you wish to uninstall and select `remove`

### unregister via the command line

``` powershell
wsl --unregister Ubuntu-18.04
```

## install single distro

go to `windows store` and search with `wsl`

### install via the command line

``` powershell
Invoke-WebRequest https://aka.ms/wsl-kali-linux-new -OutFile kali.appx -UseBasicParsing
Add-AppxPackage .\kali.appx
```

## wslconfig

as well as `wsl` there is also a `wslconfig` command

### list distros

``` powershell
wslconfig.exe /l
```

### set new default distro

``` powershell
wslconfig.exe /setdefault Ubuntu-18.04
```
