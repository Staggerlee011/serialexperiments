Title: wsl helpful commands
Date: 2020-12-11
Tags: wls, windows
Category: Blog
Summary: Set of helpful wsl commands

Quick reference commands for dealing with `wsl` in windows10

## list wsl distro

``` powershell
wslconfig.exe /l
```

## set new default distro

``` powershell
wslconfig.exe /setdefault Ubuntu-18.04
```

## restart wls distro

``` powershell
wsl.exe -t Ubuntu-18.04
```

## uninstall single distro

go into windows `apps and features` select the distro you wish to uninstall and select `remove`

## install single distro

go to `windows store` and search with `wsl`
