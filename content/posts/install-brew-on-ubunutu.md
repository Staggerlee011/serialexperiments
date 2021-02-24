---
title: "Install Brew on Ubunutu-18"
date: "2020-12-03"
summary: "Steps to install and configure brew for Ubuntu-18"
tags: [
    "brew",
    "ubuntu"
]
---

Its really simple and to be honest doesnt need a blog post, but since i managed to ignore all the warning signs, someone else might :). 

## Pre-reqs

none

## Steps

steps can be followed by reading the install as it happens, if you miss it like i did! read on:

### Install brew

the url and home of brew for linux is here: `https://brew.sh/` (this may have an updated url so please check if you get errors)

``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Configure brew

this is where i messed up! apon finishing the install, it feeds you lots of HELPFUL info saying you need to update your `PATH` and suggests installing some other software, i ignored this and spent a few hours moaning to my team that things dont work like they should and trying to workout why i could install things but not use them ><

this is an example solution! if your ubuntu login is not `stephen` this wont work for you!!!

``` bash
echo 'eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >> /home/stephen/.profile                                   
eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)  
```

it also suggests installing the below

``` bash
sudo apt-get install build-essential
brew install gcc
```

### Test

thats it, you should now be good to go and install all the lovely software and have it work properly!

``` bash
brew help
```
