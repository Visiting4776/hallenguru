### setup

1) Create a new `python3` environment: `python3 -m venv env`
2) Activate the environment and install necessary packages:
```
source env/bin/activate
python3 -m pip install -r requirements.txt
```
3) Install node packages within the `client` directory: `cd client && npm install`
4) Run server (from the root directory of the repo): `python server.py`