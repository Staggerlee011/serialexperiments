---
title: "Vale - linting for prose"
date: "2021-04-13"
summary: "Setting up and running Vale"
tags: [
    "vale", 
    "vs-code" 
]
---

You may be aware of tools like `grammerly` to assist in fixing grammar and spelling issues in your email. Vale is a similar tool, but its a `open source` cli, so can be used  to help automate and standardize your teams prose. below is there description of the production from the `github` page

``` markdown
Vale is a command-line tool that brings code-like linting to prose. It's fast, cross-platform (Windows, macOS, and Linux), and highly customizable.
```

## Install

To install `vale` you can use `brew`, for other options please see: `https://docs.errata.ai/vale/install`

``` bash
brew install vale
```

## Configuration

Add a `.vale.ini` file to the root of your repo, below is a basic example for it

``` ini
StylesPath = styles

Vocab = tech

[*.md]

BasedOnStyles = Google
```

### StylesPath

This is your root folder for 3rd party styles, language rules etc.

### Vocab

You can add single or multiple values here. Its a section for adding words that you want to ignore or highlight from your `linting`. I have added a `tech` folder and put in words like `aws`, `kubernetes` etc.

You create a folder and under your `StylesPath` with the vocab name and then add 2 files, `accept.txt` and `reject.txt`

### File types

Next list which file types you wish to run vale against example `[*.md]` will only check `markdown` files

### BasedOnStyles

This is where you pick which `styles` you want to run. In my example I have downloaded the `google` style. But many others exist (like Microsoft, Write-good, etc)

## Add a 3rd party style

Here you can just copy the folder of `yaml` rules from your chosen `style` guide, I copied the `Google` folder from `https://github.com/errata-ai/Google` under my `styles` folder

## VSCode Setup

You can install the `vscode` extension that allows you to see the suggestions in the `problems` tab, the installation is standard, search for `vale` in the extensions section. Remember to update the extensions cli settings and to `restart` `vscode` to enable it.

## Cli usage

As well as integrating it with `vscode` you can also run `vale` via the command line. The easiest option there is `cd` into the root of the folder or where ever you have the `.vale.ini`

### All files

To run `vale` against `all` files with a matching format run

``` bash
vale .
```

### Specific file

To run `vale` against a specific file

``` bash
vale content/posts/aws-configure.md
```

## Next steps

One thing that isn't available out the box is a `pre-commit` hook to add your `linting` to standard commit workflows.

The other thing to look at is do you want to use a standard `style` or create you own. I'm happy to use a standard one and have it as a simple improvement to my current writing, but you may want to refine it.

I really like the option of adding some linting to my and the teams docs proses and this is great easy option. Hope its helpful to you to.

## Resources

- [Vale docs](https://docs.errata.ai/)
- [Example boilerplate usage](https://github.com/errata-ai/vale-boilerplate)
- [vscode extension](https://github.com/errata-ai/vale-vscode)
- [Style Options](https://github.com/errata-ai/styles)
