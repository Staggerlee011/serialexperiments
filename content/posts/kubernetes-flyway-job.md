---
title: "Flyway database migrations on Kubernetes"
date: "2021-01-19"
summary: "Running flyway database migrations in kubernetes"
tags: [
    "kubernetes",
    "database"
]
---

Managing `database` migrations via code is good! back in `DBA` days i used `SSDT` and `RedGate` tools to do my SQL Server deployments. In my current shop we normally use `postgres` so I needed to find a new tool. Searching around i found `flyway` which also happens to have owned by `RedGate` and this lets you do `migration` deployments to `postgres`, `sql server`, `mysql` and a host of others im sure.

To run it locally is super easy, download the client create your conf file with the database you want to deploy to and write your `.sql` files. But when you have a more locked down production environment that you need to copy the `.sql` files into, get the tool on a box and be allow patching and all the rest of it, we ran into problems. My solution (though some may say not very elegant) is the create a `docker` image from the flyway base image load in the sql files as part of a `CI/CD` and push it to `kubernetes` Then i just needed to run it. Which is a perfect example of a `job` and pass it the conf (Hello `configmap`).

Code for the solution is below

## Dockerfile

``` docker
FROM flyway/flyway:7.3.2

RUN ["rm", "-fr", "/flyway/sql"]
COPY sql/ /flyway/sql/

ENTRYPOINT ["flyway", "migrate", "-url=jdbc:postgresql://localhost:5432/customerdb", "-user=postgres", "-password=postgres"]
```

## Kubernetes Manifests

I used a configmap to create my `flyway.conf` file. You can do it as a `secret` or I believe in pass in values as `environment variables`

ConfigMap

``` yml
apiVersion: v1
kind: ConfigMap
metadata:
  name: flyway-configmap
data:
  flyway.conf: |
    flyway.url=jdbc:postgresql://<RDS-INSTANCE>:5432/<database>
    flyway.user=<FLYWAY-ACCOUNT>
    flyway.password=<PASSWORD-FOR-ACCOUNT>
```

Then you just need a job to call the image and run it

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
          image: ECR_URL:<TAG>
          command: ["flyway", "migrate"]
          volumeMounts:
            - name: flyway-config-volume
              mountPath: /flyway/conf
      volumes:
        - name: flyway-config-volume
          configMap:
              name: flyway-configmap
      restartPolicy: Never
```

With it now being in `kubernetes` you can use `kustomize` to allow easy deployments to different environments and image upgrades. 

Hope this helps!
