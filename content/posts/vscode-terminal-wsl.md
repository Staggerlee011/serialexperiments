---
title: "vscode terminal set to wsl"
date: "2019-12-08"
description: "configure vscode terminal to use wsl"
tags: [
    "wsl",
    "vscode"
]
---

After getting myself into far to many messes with using both powershell and wsl, im moving uninstalling all things windows and trying to only run `work` apps via the wsl ubunutu image. with that i stil use vscode for all my coding and having the terminal open for all comamnds that i need. To update it to use wsl is super easy via

## Steps to update vscode default terminal

- open the terminal
- select the drop on the right hand side dropdown bar
- select "Select default shell"

![image of terminal](images/vscode-terminal-wsl-01.JPG)

**This opens the command palette with the options you cna switch to**

![vscode command palette](images/vscode-terminal-wsl-02.JPG)

- select WSL bash

## Common issues

i found that my default wsl image was docker when setting this up. So after completing the above I would then get an error saying 

``` powershell
The terminal process "C:\Windows\System32\wsl.exe" failed to launch (exit code: 1).
```

![error from vscode for wsl](images/vscode-terminal-wsl-03.png)

The fix is to update wsl and set the ubuntu image as your default wsl:
  
running the below will list out all your wsl images as well inidicate which is your current default:

``` powershell
wslconfig.exe /l
```

run the below to update it to your prefered disto:

``` powershell
wslconfig.exe /setdefault Ubuntu-18.04
```

confirm via running `wslconfig` again

![wslconfig default image](images/vscode-terminal-wsl-04.png)

You should now be able to open wsl from vscode

## References

- [vscode termianl integrations](https://code.visualstudio.com/docs/editor/integrated-terminal)
- [troubleshooting vscode terminal launch](https://code.visualstudio.com/docs/supporting/troubleshoot-terminal-launch)
