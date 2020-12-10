Title: Create a pelican blog
Date: 2020-12-11
Tags: pelican, python
Category: Blog
Summary: Inital steps to setup a pelican blog

Inital steps to create a pelican blog (like this one) are below:

## pre-reqs

- python3 installed
- python virtualenvironment installed

## folder

set up a folder to work from

``` bash
mkdir blog
cd blog
```

## set up python virtual environment

next we create our python virtual environment to manage our dependencies and activate it

``` python
python3 -m venv env
source env/bin/activate
```

**Note you should now see (env) at the start of your command prompt**

## install python dependencies

install pelican and other dependencies

``` python
pip install pelican, Markdown, typogrify
pip freeze > requirements.txt
```

## create the blog template

create a base pelican site, filling in the details as you see fit

``` python
pelican-quickstart
```

## test

you can now either run make devserver to test the site (i just keep this running while developing on pelican)

``` bash
make devserver
```

## Add pelican themes

stylise your site with one of the many pelican themse (More can be found [here](http://www.pelicanthemes.com/)), ill download my favourite voce

```
mkdir themes
cd themes
git clone https://github.com/limbenjamin/voce
cd ..
```

update `pelicanconf.py` with the new theme path

``` python
THEME = 'themes/voce'
```

## plugins

Add some plugins (i like [pelican-gist](https://github.com/streeter/pelican-gist))

``` python
pip install pelican-gist
pip freeze > requirements.txt
```

update your `pelicanconf.py` with the new plugin

``` python
PLUGINS = [
    'pelican_gist',
]
```

## add content

create a `new-blog.md` file in the `content` folder 

``` markdown
make devserver
```

## view site

if you dont have the site up and running, run `make devserver` you should now have a new pelican site, with theme and a plugun running :)
