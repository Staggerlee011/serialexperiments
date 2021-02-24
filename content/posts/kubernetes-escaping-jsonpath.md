---
title: "Escaping kubernetes jsonpath"
date: "2021-02-24"
description: "Note on how to escape when using `-o jsonpath=` in kubernetes"
tags: [
    "kubernetes",
]
---

This came up today when I created a `sealedsecret` and wanted to confirm the secret had the correct value. Normally I can just use `-o jsonpath="{.data.password}` to parse out the `json` value I want, but this time the value I wanted was like `myfile.conf` so `jsonpath` came up empty as there it was looking for a path that didn't exist. The answer is to escape out with the below:

``` yaml
k get secrets mysecret -o jsonpath="{.data.myfile\.conf} 
```
