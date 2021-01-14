---
title: "Serverless Framework by Example"
date: "2021-01-14"
description: "Example setup and usage of the Serverless Framework with AWS and python"
tags: [
    "python",
    "aws",
    "serverless"
]
---

At present I'm using the `serverless framework` to deploy and manage all my `lambda` functions. For more details on how to use `serverless framework` please see my links at the bottom of the post. These are examples are quick `templates` I use to cut and paste into new projects to get going a bit quicker.

<!-- TOC -->

- [Basics](#basics)
  - [Create a new project](#create-a-new-project)
  - [Deploy project](#deploy-project)
  - [Test Function](#test-function)
  - [Serverless.yml template](#serverlessyml-template)
- [Plugins](#plugins)
  - [Add a plugin](#add-a-plugin)
  - [Serverless-iam-roles-per-function](#serverless-iam-roles-per-function)
    - [Usage](#usage)
    - [Add serverless-iam-roles-per-function](#add-serverless-iam-roles-per-function)
    - [Add to servereless.yml](#add-to-serverelessyml)
- [Serverless.yml setup](#serverlessyml-setup)
  - [CRON job](#cron-job)
  - [Using SSM values](#using-ssm-values)
  - [Deploy function to VPC](#deploy-function-to-vpc)
- [References](#references)

<!-- /TOC -->

## Basics

Collection of simple snippets to get started

### Create a new project

Creates a new `serverless.yml` and framework files. To deploy to a specific folder add `-p` and the name of the folder you want

``` bash
sls create --template aws-python3
```

### Deploy project

We used `aws named profiles` if you are deploying straight to the `default` profile you can remove the switch

``` bash
sls deploy --aws-profile <aws profile>
```

### Test Function

To test a single function deployed you can run `invoke`

``` bash
sls invoke -f <function name> --aws-profile <aws profile>
```

### Serverless.yml template

below is starting template for serverless that sets up the following:

- secure s3 bucket (Blocks public access and encrypted at rest)
- Adds some standard tags (`serverless` = `true`)
- iam separation per function using the plug `serverless-iam-roles-per-function`

``` yml
service:
  name: ${self:custom.application}
frameworkVersion: '2.4.0'

custom:
  application: ses-test

provider:
  name: aws
  runtime: python3.8
  region: eu-west-2
  stackName: ${self:custom.application}
  tags: 
    Application: ${self:custom.application}
    Serverless : "true"
  deploymentBucket:
    maxPreviousDeploymentArtifacts: 1 
    blockPublicAccess: true 
    serverSideEncryption: AES256
    tags:
      Application: ${self:custom.application}
      Serverless : "true"     

functions:
  ses-test:
    name: "ses-email-test"
    description: "sends a test email from ses"
    handler: functions/ses-test.handler
    timeout: 60
    iamRoleStatementsName: ses-test-role
    iamRoleStatements:
      - Effect: "Allow"      
        Action:
          - ses:SendEmail
          - ses:SendRawEmail
        Resource: "*"
      - Effect: "Allow"      
        Action:
          - logs:CreateLogGroup
          - logs:CreateLogStream
          - logs:PutLogEvents
        Resource: "arn:aws:logs:*:*:*"

plugins:
  - serverless-iam-roles-per-function
```

## Plugins

### Add a plugin

To add a plugin you will need to add it under the `plugins:` section of `serverless.yml` 

``` yml
plugins:
  - serverless-iam-roles-per-function
```

You will also need to load the npm of the plugin:

``` bash
npm install serverless-iam-roles-per-function
```

Below are regular plugins I use and there configs

### Serverless-iam-roles-per-function

This plugin allows you set individual `iam` roles per function instead of the standard single `iam` for all.

NOTE: serverless-iam-roles-per-function stopped working on serverless@2.5 ensure you install serverless to 2.4!!!

#### Usage

The below example creates a `iam` role called `ses-test-role` with specific permissions to `ses` and `logs`

** NOTE: Always add the `logs` action for monitoring of the function  

``` yml
    iamRoleStatementsName: ses-test-role
    iamRoleStatements:
      - Effect: "Allow"      
        Action:
          - ses:SendEmail
          - ses:SendRawEmail
        Resource: "*"
      - Effect: "Allow"      
        Action:
          - logs:CreateLogGroup
          - logs:CreateLogStream
          - logs:PutLogEvents
        Resource: "arn:aws:logs:*:*:*"
```

#### Add serverless-iam-roles-per-function

``` bash
npm install serverless-iam-roles-per-function
```

#### Add to servereless.yml

``` yml
plugins:
  - serverless-iam-roles-per-function
```

## Serverless.yml setup

Collection if snippets to use in `serverless.yml`

### CRON job

Setting up a `cron` job for a function

``` yml
functions:
  start-rds:
    name: "start-rds"
    description: "start rds instances based on tagging"
    handler: functions/start-rds.handler
    timeout: 60
    iamRoleStatementsName: start-rds-role
    iamRoleStatements:
      - Effect: "Allow"      
        Action:
          - rds:*
        Resource: "*"
      - Effect: "Allow"      
        Action:
          - logs:CreateLogGroup
          - logs:CreateLogStream
          - logs:PutLogEvents
        Resource: "arn:aws:logs:*:*:*"
    events:
      - schedule: cron(00 08 ? * MON-FRI *) # 08:00 on every day-of-week from Monday through Friday.
```

### Using SSM values

I like separating config out and using ssm to store it

``` yml
functions:
  example:
    name: "example-ssm"
    description: "example function that pulls a value from ssm"
    handler: functions/example.handler
    timeout: 60
    iamRoleStatementsName: example-ssm-role
    iamRoleStatements:
      - Effect: "Allow"
        Action:
         - ssm:*
        Resource: "*"
    vpc:
      securityGroupIds:
        - ${ssm:/global/sec/serverless/id~true}
      subnetIds:
        - ${ssm:/global/subnets/intra/az/a/id~true}
        - ${ssm:/global/subnets/intra/az/b/id~true}
```

### Deploy function to VPC

Deploy a function to a `VPC` and specific subnets

``` yml
functions:
  my-function:
    name: "My Function"
    description: "Lambda function"
    handler: functions/example.handler 
    timeout: 20
    vpc:
     securityGroupIds:
      - ${ssm:/global/sec/serverless/id~true}
     subnetIds:
      - ${ssm:/global/subnets/intra/az/a/id~true}
      - ${ssm:/global/subnets/intra/az/b/id~true}
```

## References

Collection of primary resources to troubleshoot and learn more:

- [Serverless Framework Reference Doc](https://www.serverless.com/framework/docs/providers/aws/guide/serverless.yml/)
