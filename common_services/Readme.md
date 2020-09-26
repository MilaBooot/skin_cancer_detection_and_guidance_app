# Common Services API
The services are written in python3.6
## Install the pip requirements
```
pip install -r requirements.txt
```
## Set the environment variable
 ```
 RDS_HOSTNAME=localhost
 ```
 THE environment variable is set by AWS automatically when an RDS DB is created in the environment. To run locally set RDS_HOSTNAME environment variable in
## Run the Flask server
HTTP server:
```
python common_services/application.py
```

The common services api will be launched at port 5000 (localhost:5000)

 - Swagger UI: localhost:5000