---
title: "Kubectl port forwarding - address already in use"
date: "2021-01-26"
summary: "Collection of resources for learning / managing EKS"
tags: [
    "kubernetes",
    "linux"
]
---

Quick note on if you see an error like below:

``` bash
$ k port-forward pgadmin -n pgadmin 8080:80
Unable to listen on port 8080: Listeners failed to create with the following errors: [unable to create listener: Error listen tcp4 127.0.0.1:8080: 
bind: address already in use unable to create listener: Error listen tcp6 [::1]:8080: bind: address already in use]
error: unable to listen on any of the requested ports: [{8080 80}]
```

This is caused by `kubectl` not releasing its port binding. You can manually `kill` the `pid` via the below (Example is based on trying to run a `8080` port forward)

``` bash
lsof -i :8080
```

After getting the `pid` you can then kill it via the standard `kill -9 12345`
