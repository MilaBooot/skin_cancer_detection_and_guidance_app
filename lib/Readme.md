# Common Services API
The services are written in python3.6
## Install the pip requirements
```
pip install -r requirements.txt
```

## Run the Flask server
HTTP server:
```
FLASK_APP=lib/api_server.py flask run
```
HTTPS server:
```
FLASK_APP=lib/api_server.py flask run --cert adhoc
```

The common services api will be launched at port 5000 (localhost:5000)

 - Sagger UI: localhost:5000