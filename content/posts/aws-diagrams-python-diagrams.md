---
title: "AWS Diagrams via Python Diagrams"
date: "2020-12-30"
summary: "Create AWS diagrams from python"
tags: [
    "python",
    "aws",
]
---

I'm always on the hunt for an easy way to create good architecture diagrams, I would love to be good at `visio` but anyone who has worked with me will tell you am I most definitely note. So the idea of creating diagrams via code is definitely something that interests me.

## Python Diagrams

[Github - diagrams](https://github.com/mingrammer/diagrams)
  
Diagrams is a python package that lets you create some very pretty diagrams via code. It outputs a `.png` file, lets do a quick example:

## Setup

To use diagrams you first need to install graphviz, I try and keep to a central package manager and currently use `brew` but you can also install it numerous ways as well as `choco install graphviz -y` for Windows.

``` python
brew install graphviz
```

We then need to set up a python environment that is `3.6+`, I create a virtual environment, install diagrams and output that to a `requirements.txt`

``` python
# create virtualenv
python3 -m venv env
source env/bin/activate
## install diagrams
python3 -m pip install diagrams
python3 -m pip freeze > requirements.txt
```

## Create a diagram

There's lots of example on the site, but I created a simple one creating a file called `my-app-diagram.py` with the below code:

``` python
from diagrams import Cluster, Diagram
from diagrams.aws.network import VPC, ELB
from diagrams.aws.compute import EKS
from diagrams.aws.mobile import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS

with Diagram("My-app", show=False):
    lb = ELB("lb")
    k8s = EKS("EKS Cluster")
    igw = APIGateway("API Gateway")

    with Cluster("Lambda Functions"):
        svc_group = [Lambda("fnc1"),
                     Lambda("fnc2"),
                     Lambda("fnc3")]
    
    rds = RDS("Postgres RDS")
    lb >> k8s >> igw >> svc_group >> rds
```

Nothing to scary in there, we `import` all the icons we want to use open a `with` set the name of the diagram and start listing all the objects. Then at the bottom we link them together via `>>`.

## Generate a diagram

To generate the diagram we then just run the python script:

``` python
python3 my-app-diagram.py
```

This creates a file called `my-app.png` which looks like this:

![Example diagram from python diagram](/python-diagrams/my-app.png)

And there we have it, there's a lot of nice examples in the diagrams repo to look through, but I'm currently a bit of a fan to say the least. I think it would fall down if you're trying to diagram a AZ, EC2 heavy environment and I've not found a good example of doing that, but for simple diags it looks a really nice choice.
