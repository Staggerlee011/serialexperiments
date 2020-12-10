Title: Create a pelican blog
Date: 2020-12-11
Tags: pelican, python
Category: Blog
Summary: Inital steps to setup a pelican blog


```
mkdir blog
cd blog
python3 
```

setup:
```
pip install pelican, Markdown, typogrify
```

create blog:
```
pelican-quickstart
```

theme:

```
mkdir themes
cd themes
git clone https://github.com/limbenjamin/voce
```



## plugins

pip install pelican-gist

pip freeze > requirements.txt



run:

```
make devserver
```
