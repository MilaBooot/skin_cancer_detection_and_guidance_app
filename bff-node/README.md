# Read Me First
Backend-for-Frontend (BFF) developed using Java and Spring Boot
# Getting Started
####Requirement
                
1. Java 8+
2. Gradle 6+

                

####Build Code

`$ gradle clean build -xtest`


####Run

`$ start.bat`


###Links

`<swagger-url>` : <https://localhost:8080/bff/api/swagger-ui.html>



####Configurable by property file

`server.port=8080`
`common.service.url=http://<host>:<port>/common-service/api #common-service url`
`common.service.user.registration.endpoint=/register  #user registration endpoint` 