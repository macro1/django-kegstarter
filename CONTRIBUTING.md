Setup
=====

Python
------
* Python 3.4+
* Setup a virtual env
* `cd backend`
* `pip install -e .\[dev\]`

If you local development can be done with SQLite, but a real deployment
should use Postgres.

Ember
-----
* Node v0.12.4 and NPM 2.10.1 (on OSX also using nodenv)
* `cd frontend`
* `npm install`
* `bower install`
* `ember serve`

This assumes that you have `./node_modules/.bin` in your path.
