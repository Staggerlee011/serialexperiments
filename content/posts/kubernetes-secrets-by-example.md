---
title: "Kubernetes Secrets by Example"
date: "2021-01-21"
description: "Examples to create and use kubernetes secrets"
tags: [
    "kubernetes",
]
---

Collection of `kubernetes` secrets by example:

## Create secret

Examples of how to create a `secret`

### --from-literal

Creates the manifest file from the command line:

``` bash
k create secret generic wordpress-user-password --dry-run=client --from-literal password=MySuperSecretPassword --output yaml
```

You can pass multiple `--from-literal` values into the secret if you wish

### --from-file

Create a secret from a file (ie a txt file with a password in it)

NOTE: When creating a secret from file remember the name of the file is used as the key ie: mypassword.txt = MySuperSecretPassword for below

``` bash
echo MySuperSecretPassword | tee mypassword.txt
```

You can then create a `secret` from the file

``` bash
k create secret generic wordpress-user-password --dry-run=client --from-file=./mypassword.txt --output yaml
```

You can pass multiple `--from-file` values into the secret if you wish


## See Secrets in Kubernetes

Collection of example commands to see secrets you have put in kubernetes

### List secrets

``` bash
k get secrets pgadmin-secret -o yml
```

### Get secret value

``` bash
k get secrets pgadmin-secret -o jsonpath="{.data.password}" | base64 --decode && echo
```

## Use secret

Once you have created a secret we now can use it via:

### Expose secret as a environment variable to container

In this example we will create a secret to use with `pgadmin`. To run `pgadmin` you need to pass it a default user and password via `environmental variables`.

Create the secret via

``` bash
k create secret generic pgadmin-secret --dry-run=client \
--from-literal email=admin@admin.com \
--from-literal password=SuperSecretPassword \
--output yaml
```

secret manifest would look like:

``` yml
apiVersion: v1
data:
  email: YWRtaW5AYWRtaW4uY29t
  password: U3VwZXJTZWNyZXRQYXNzd29yZA==
kind: Secret
metadata:
  creationTimestamp: null
  name: pgadmin-secret
```

We would then use the secrets via:

```yml
apiVersion: v1
kind: Pod
metadata:
  name: pgadmin
spec:
  containers:
  - name: pgadmin
    image: 991775749516.dkr.ecr.eu-west-2.amazonaws.com/pgadmin:4.28
    env:
    - name: PGADMIN_DEFAULT_PASSWORD # name of the environmental var
      valueFrom:
        secretKeyRef:
          name: pgadmin-secret # name of the secret 
          key: password # name of the key in the secret
    - name: PGADMIN_DEFAULT_EMAIL
      valueFrom:
        secretKeyRef:
          name: pgadmin-secret
          key: email
```

### Pass secret to file in container

You can also create a file (like you can with `configMaps`) that you can pass to a container. This can be a solution to idea of not wanting to put passwords into `configMaps` but it does then put all that text and keys into the `secret` that you don't need (A good solution for that will be in a future post!).

Create a secret to file:

``` yml
apiVerison: v1
kind: Secret
metadata:
  name: flyway-secret
type: Opaque
data:
  flyway.secret: |
    flyway.url=jdbc:postgresql://<RDS-INSTANCE>:54321/db
    flyway.user=<FLYWAY-ACCOUNT>
    flyway.password=<PASSWORD-FOR-ACCOUNT>
```

Deploy a container with the file attached via a volume

``` yml
apiVersion: batch/v1
kind: Job
metadata:
  name: flyway
spec:
  template:
    metadata: 
      name: flyway
    spec:
      containers:
        - name: flyway
          image: flyway/flyway
          command: ["flyway", "migrate"]
          volumeMounts:
            - name: flyway-secret-volume
              mountPath: /flyway/conf
      volumes:
        - name: flyway-secret-volume
          secret:
              name: flyway-secret
      restartPolicy: Never
```

## Decode kubernetes secret

This section is a quite reminder / steps to show why `kuberetes` secrets should not be in source control:

You can create a kubernetes secret via:

``` bash
k create secret generic wordpress-user-password --dry-run=client --from-literal password=MySuperSecretPassword --output yaml
```

this would generate:

``` yaml
apiVersion: v1
data:
  password: TXlTdXBlclNlY3JldFBhc3N3b3Jk
kind: Secret
metadata:
  creationTimestamp: null
  name: wordpress-user-password
```

We can reserve the `secret` via (Hence why we should not leave `secrets` in source control):

``` bash
echo TXlTdXBlclNlY3JldFBhc3N3b3Jk | base64 --decode
```


## Resources

- [Kubernetes secrets doc](https://kubernetes.io/docs/concepts/configuration/secret/)
- [YouTube Video - ThatDevOps Guy - Kubernetes Secret Management Explained](https://www.youtube.com/watch?v=o36yTfGDmZ0)
- [SealedSecrets by Example](https://blog.serialexperiments.co.uk/posts/kubernetes-sealedsecrets-by-example/)
  