# flask-vue
Flask and Vue playing happily together


## Inspiration
Flask and Vue use similar templating, making them incompatible out of the box. In this example I have modified the default flask tokens and built a flask application that serves a vue frontend.

## Prerequisites
I'm using [pipenv](http://docs.pipenv.org/) for my python dependencies.

    $ pip install pipenv 
    $ # although I had to run the following to get it to install on my mac without warnings
    $ sudo -H pip install --ignore-installed pipenv

## Installation
    $ git clone git@github.com:texuf/flask-vue.git
    $ cd flask-vue/server
    $ pipenv install

## Server
    $ cd flask-vue/server
    $ pipenv run python app.py 

## Work on Client
    $ # in a second terminal window
    $ cd flask-vue/client
    $ # setup any sass / npm / bootstomper / whatevers here, have the build scripts output to `server/static`


## Resources
- [pipenv](http://docs.pipenv.org/)
- [flask](http://flask.pocoo.org/)
- [vue](https://vuejs.org/v2/guide/)

### Tips
- Try a `hard refresh` if you're not seeing your js files update when you change them [stack overflow](https://stackoverflow.com/questions/41144565/flask-does-not-see-change-in-js-file)
-- Windows: Ctrl+F5
-- Mac: Cmd+Shift+R
-- Linux: Ctrl+Shift+R