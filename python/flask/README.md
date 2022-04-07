
### Install

Use [venv][] or any other ([Pipenv][], [Poetry][], etc) [environment management][] tool to install dependencies in the same folder.
Activate virtual environment and run:

``` bash
pip install -r requirements.txt
```

### Launch

After you have database server deployed and running, use environment variable `DATABASE_URL` to provide database connection string.

> `FLASK_ENV` is set to `development` by default.

``` bash
DATABASE_URL=postgres+psycopg2://user:password@127.0.0.1:5432/postgres python run.py
```

Go to <http://127.0.0.1:5000/> in your browser.

Refer to [API.md](../../API.md) for available endpoints and methods.

[Flask]: http://flask.pocoo.org/
[venv]: https://docs.python.org/3/tutorial/venv.html
[Pipenv]: https://pipenv.pypa.io/en/latest/
[Poetry]: https://python-poetry.org/docs/
[environment management]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
