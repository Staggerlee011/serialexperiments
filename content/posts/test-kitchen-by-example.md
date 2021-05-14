---
title: "test-kitchen with ansible, ec2 and inspec"
date: "2023-04-22"
summary: "template and steps to set up a test-kitchen with ansible, ec2 and inspec"
tags: [
    "ansible",
    "test-kitchen",
    "inspec"
]
---

I've been doing some clean of our image builds. With that I've wanted to add in `test-kitchen` to process as its a nice wrapper to allow for running and re-running tests and ansible playbooks without to much leg work. If you don't know `test-kitchen` or sometimes called `kitchenci` take a look here: `https://github.com/test-kitchen/test-kitchen`

## Pre-reqs

`test-kitchen` is a rubyGem and can either be installed via `gem install test-kitchen` or as part of the `chef workstation`. As we are also planning on using inspec, i went with the later. I use `bundle` to manage the deployment of `gems` and ruby as 
