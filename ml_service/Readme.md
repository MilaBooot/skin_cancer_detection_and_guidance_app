# ML prediction Services API
The services are written in python3.6
## Install the pip requirements
```
pip install -r requirements.txt
```

## Run the Flask server
HTTP server:
```
FLASK_APP=ml_service/ml_api.py flask run --port 5001
```

The common services api will be launched at port 5000 (localhost:5000)

 - Swagger UI: localhost:5001