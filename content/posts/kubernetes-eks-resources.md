---
title: "EKS Resources"
date: "2021-01-25"
summary: "Collection of resources for learning / managing EKS"
tags: [
    "kubernetes",
    "eks"
]
---

## Networking

### Security Groups for Pods

- If you use the `default` CNI `aws-node` then you are limited to hosting a number of pods based on the instance type:

`https://docs.amazonaws.cn/en_us/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI`

- If you wish to use `security groups for pods` you have to use a `ec2` type on the list below:

`https://docs.amazonaws.cn/en_us/eks/latest/userguide/security-groups-for-pods.html#supported-instance-types`

- If you have ran `kubectl set env daemonset aws-node -n kube-system ENABLE_POD_ENI=true`  and still see `vpc.amazonaws.com/has-trunk-attached=false` for all nodes in the cluster. Try rotating your nodes (ie auto-scaling instance refresh) OR Again checking if you nodes are on the `supported instance types` list above (This was our problem! and wasted half of my day :()

#### Troubleshooting

- You can safely ignore the below the logs which can be seen in `k describe pod`

``` bash
Normal   SecurityGroupRequested  8m18s  vpc-resource-controller  Pod will get the following Security Groups [sg-01abfab8503347254]
  Normal   ResourceAllocated       8m17s  vpc-resource-controller  Allocated [{"eniId":"eni-0bf8102e8bf0fa369","ifAddress":"02:78:59:8f:ee:b2","privateIp":"10.243.50.203","vlanId":1,"subnetCidr":"10.243.48.0/20"}] to the pod
  Warning  FailedCreatePodSandBox  8m17s  kubelet                  Failed to create pod sandbox: rpc error: code = Unknown desc = failed to set up sandbox container "bdacc9416438c30c46cdd620a382a048cb5ad5902aec9bf7766488604eef6a60" network for pod "pgadmin": networkPlugin cni failed to set up pod "pgadmin_pgadmin" network: add cmd: failed to assign an IP address to container
  Normal   SandboxChanged          8m16s  kubelet                  Pod sandbox changed, it will be killed and re-created.
```

- You can see if your pod has connected to the `sg` and `eni` via running a `k describe pod..` as you should get an output like:

``` bash
Annotations:  kubernetes.io/psp: eks.privileged
              vpc.amazonaws.com/pod-eni:
                [{"eniId":"eni-0bf8102e8bf0fa369","ifAddress":"02:78:59:8f:ee:b2","privateIp":"10.243.50.203","vlanId":1,"subnetCidr":"10.243.48.0/20"}]
    Limits:
      vpc.amazonaws.com/pod-eni:  1
    Requests:
      vpc.amazonaws.com/pod-eni:  1
```

As well as the logs from describe showing:

``` bash
Pod will get the following Security Groups [sg-01abfab8503347254]
```
