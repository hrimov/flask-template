# Flask template

This repo will contain several project structure templates
for Flask:

- [MVC](https://github.com/hrimov/flask-template/tree/structure/MVC)
- Layered (**current branch**)

# Installation

Just clone the repo and run `poetry install`.
For the checking example route at `localhost:5000/users/`
you should have running Postgres with applied migration and simply run `python -m app`.

# Advantages

- No `flask_sqlalchemy`, which is using globals
- No applications globals, e.g. `Flask` application, session and etc
- N-Layered architecture is very scalable

# Disadvantages

- N-Layered design takes more development time to set up
  and stick to it
