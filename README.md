# flask-vue
Flask and Vue playing happily together


## Inspiration
Flask and Vue use similar templating, making them incompatible out of the box. In this example I have modified the default flask template tokens and built a flask application that serves a vue frontend.

The server returns `index.html` which blends jinja and vue templates. `app.js` modifies the vue templates and fetches and displays data from `api/data/<parameter>`

## Prerequisites
I'm using [pipenv](http://docs.pipenv.org/) for my python dependencies.

    $ pip install pipenv 
    $ # is supposed to "work"
    $ # I had to run the following to get pipenv on my mac without warnings
    $ sudo -H pip install --ignore-installed pipenv

## Installation
    $ git clone git@github.com:texuf/flask-vue.git
    $ cd flask-vue/server
    $ pipenv install

## Run Server
    $ cd flask-vue/server
    $ pipenv run python app.py 
    ...
    $ open http://127.0.0.1:5000/

## Work on Client
    $ # in a second terminal window
    $ cd flask-vue/client
    $ # setup any sass / npm / bootstomper / whatevers here, have the build scripts output to `server/static`


## Resources
- [pipenv](http://docs.pipenv.org/)
- [flask](http://flask.pocoo.org/)
- [vue](https://vuejs.org/v2/guide/)

## Other flask/vue apps
- https://github.com/lh00000000/vue-flask-template
- https://github.com/JulienBalestra/vue-flask
- https://github.com/ioiogoo/Vue-News-Board
- https://github.com/taogeT/flask-vue

## Deploying to heroku
Install the heroku cli: https://devcenter.heroku.com/articles/getting-started-with-python

    $ cd flask-vue/server
    $ pipenv install gunicorn
    $ echo web: gunicorn app:app > Procfile
    $ cd ../
    $ git add -A && git commit -m "Added Procfile and Gunicorn"
    $ heroku create
    $ git subtree push --prefix server heroku master
    $ heroku logs --tail

### Tips
- Try a `hard refresh` if you're not seeing your js files update when you change them. _[link](https://stackoverflow.com/questions/41144565/flask-does-not-see-change-in-js-file)_
   - Windows: Ctrl+F5
   - Mac: Cmd+Shift+R   
   - Linux: Ctrl+Shift+R
