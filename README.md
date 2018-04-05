Simple example for management users (add and list) with MongoDB or SQL.

## Usage MongoDB:

* Install requirements:
```bash
$ pip install -r mongodb/requirements.txt
```

* Run:

```bash
$ python mongodb/run.py
```
Open in your browse: http://127.0.0.1:5000/usuarios/

## Usage SQL:

* Install requirements:

```bash
$ pip install -r sql/requirements.txt
```

* Migrate database:

``` bash
$ python sql/Model/Model.py db migrate
```
 Run:

```bash
$ python sql/run.py 
```
Open in your browse: http://127.0.0.1:5000/usuarios/
