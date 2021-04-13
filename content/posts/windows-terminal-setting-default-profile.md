---
title: "Setting the Default Profile for Windows Terminal"
date: "2021-02-12"
summary: "Steps to change the default profile on Windows Terminal from PowerShell to WSL"
tags: [
    "windows-terminal",
    "workstation"
]
---

I don't use `windows-terminal` much. But I do find that I want it to be my `WSL Ubuntu-18` profile instead of `PowerShell`. To set that up you just need to:

## Get Profile ID for Desired Profile

Open `Windows Terminal` -> `Settings` this opens the `settings.json`

![Windows Terminal Settings](/win-terminal/windows-terminal-settings01.png)

Below is an example:

``` json
{
    "$schema": "https://aka.ms/terminal-profiles-schema",
    "profiles" : 
    [
        {
            "guid" : "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
            "icon" : "ms-appx:///ProfileIcons/{61c54bbd-c2c6-5271-96e7-009a87ff44bf}.png",
            "name" : "Windows PowerShell",
            "startingDirectory" : "%USERPROFILE%",
            "useAcrylic" : false
        },
        {
            "guid": "{c6eaf9f4-32a7-5fdc-b5cf-066e8a4b1e40}",
            "hidden": false,
            "name": "Ubuntu-18.04",
            "source": "Windows.Terminal.Wsl",
            "snapOnInput" : true,
            "startingDirectory": "/mnt/e"
        },
        {
            "guid": "{46ca431a-3a87-5fb3-83cd-11ececc031d2}",
            "hidden": false,
            "name": "kali-linux",
            "source": "Windows.Terminal.Wsl"
        }
    ],
```

Note the `guid` for the profile you want to use.

## Update the setttings.json defaultprofile

Add `json` name of `defaultProfile` with the `guid` of your chosen `profile` like below:

``` json
{
    "$schema": "https://aka.ms/terminal-profiles-schema",
    "defaultProfile": "{c6eaf9f4-32a7-5fdc-b5cf-066e8a4b1e40}",
    "profiles" : 
```

Save and close.
