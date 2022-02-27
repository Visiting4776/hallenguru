**Demo:** https://hallenguru.herokuapp.com/

Quickly find public pools in Berlin where time slots are still available for purchase.

![screenshot](https://user-images.githubusercontent.com/15891394/155847162-e5e26cc1-07eb-45c4-a927-9e4a728a3bd6.jpg)


### setup

1) Create a new `python3` environment: `python3 -m venv env`
2) Activate the environment and install necessary packages:
```
source env/bin/activate
python3 -m pip install -r requirements.txt
```
3) Install node packages within the `client` directory: `cd client && npm install`
4) Run server (from the root directory of the repo): `python server.py`
