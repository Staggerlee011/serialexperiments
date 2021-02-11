---
title: "VSCode Todo Tree"
date: "2020-12-17"
description: "Basic usage of the vscode extension todo-tree"
tags: [
    "vscode",
    "workstation"
]
---

Todo-tree is a handy little extension to track issues and comments in your code (I'm not going to get into the debt of weather you should put a TODO comment in code or in story board that for you decide). It adds a new pane to vscode letting you quickly look a repo/pages outstanding issues, or things to note see blow

![Image of vscode extension todo-tree](/vscode-todotree/image01.PNG)

Its really simple to use (you add a `TODO` into your code and new line pop ups in the pane, showing where it is), but I couldnt find the default options where on the extensions site: `https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree` or an easy guide to customize it should i want to.

## Standard options

By installing you get the options of:

``` python
TODO: Creates a todo note

FIXME: Creates a bug like note
```

## Customize via palette

You can add a new tag via opening the `Command Palette` and typing in `Todo Tree: add tag` you then populate it with the name of the tag (say `NOTE`) and job done you can add a note (it looks like this:)

![Default new tag example](/vscode-todotree/image02.PNG)

As you can see it uses the same icon as `TODO`, so while quick and easy to add, not great.

## Cusotmize via settings.json

If you want to add your own `tag` with a whole bunch of customization options! (read the docs for more info) then you need to edit a file, this is where i got lost as most examples talk about editing a file, but i could never see what file they edited was!. Turns out its the `settings.json` in vscode. This file is used by all extensions so be careful as you dont want to mess other extensions up when your `Todo-tree`. 

To edit `settings.json` open the `Command Palette` and type: `Preferences: Open Settings (JSON)` then add in your customized code. Theres a few out there if you google around, i like [jsonasbn dev blog post](https://dev.to/jonasbn/til-todo-tree-a-nifty-vscode-extension-16j5) (Note if you use hes copy the updated code in the comments). 

Mine currently is currently:

``` json
    "todo-tree.highlights.defaultHighlight": {
        "type": "text-and-comment"
    },
    "todo-tree.general.tags": [
        "TODO",
        "FIXME",
        "NOTE"
    ],
    "todo-tree.highlights.customHighlight": {
        "TODO": {
            "foreground": "black",
            "background": "#22B965",
            "iconColour": "#22B965",
            "icon": "squirrel",
        },
        "FIXME": {
            "foreground": "black",
            "background": "#B4292B",
            "iconColour": "#B4292B",
            "icon": "bug"
        },
        "NOTE": {
            "foreground": "black",
            "background": "#2B6DD5",
            "iconColour": "#2B6DD5",
            "icon": "octoface"
        }
    }
```

I was trying to get the colours from the ubuntu wsl as like them against the dark theme in vscode, but there not quiet right. but after spending far to long playing around with it this will do for now! :)

It gives me the below

![My todo-tree settings](/vscode-todotree/image03.PNG)

As a note you can pick the icons from the [octicons](https://primer.style/octicons/) and thats it. hope this helps.
