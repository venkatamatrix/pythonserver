# Python Flask REST Microservice  For ManagementServer Service

REST API written in Python Flask using SQLAlchemy as the ORM with auto migration capabilities

## Pre-requisites
  - Download & install [Python 3.6](https://www.python.org/downloads/)
  - Download & install [Pipenv](https://docs.pipenv.org/)
   ```bash
    python -m pip install -U pip 
   ```
  - Download & Install [MySQL](https://www.mysql.com/) Server locally or use an external database (OPTIONAL)

## For Developers
  - Download & install [NodeJS](https://nodejs.org/en/download/) 
  - Install nodemon (use sudo if you in linux)
  ```bash
  npm i -g nodemon
  ```

## Installation

  ```bash
  # Clone the repository 
 https://mattareddy.syamala@innersource.accenture.com/scm/acpicp/managementServers-service.git
  # Change into the directory
  cd managementServers-service
  # Install all required dependencies with
  pipenv install --deploy --skip-lock
  # Activate the project virtual environment
  pipenv shell
  # Create an local .env file and replace with the relevant values
  cp .env.sample .env
  ```
  You can also set the enviroment variables explicity (OPTIONAL)
  
  ```bash
  PORT=9000
  BUILD_DEV=development
  DATABASE_URL=mysql+pymysql://user:pass@host:port/dbname
  ```
## Database Auto migration & creation

You can create the tables using the following set of commands

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Running the application

  **Start the app**
  ```bash
  python run.py
  ```
  **Start the app for developers**
  ```bash
  nodemon run.py
  ```
## Usage

**API Specifications**
  - GET: /managementServers/allManagementServers
  - GET: /managementServers/{mgmtServerId}
  - GET: /managementServers/activeMgmtServers
  - POST: /managementServers
  - PUT: /managementServers/{mgmtServerId}
  - DELETE: /managementServers/{mgmtServerId}/{loggedInUser}
 

**Example**
Get all managementServers
curl http://localhost:{PORT}/managementServers
Get some managementServers-perticular
curl http://localhost:{PORT}/managementServers/1,2,3,4,

## Running the application as a Docker container
 ```bash
 cd managementServers-api
 # Build the docker image 
 docker build -t icp-managementServers .
 # Run the docker container and put the port as specified in the .env file
 docker run -d -p 7000:7000 --name icp-managementServers -e PORT=7000 -e BUILD_ENV='development' -e DATABASE_URL='mysql+pymysql://user:pass@host:port/dbname' -e DATABASE_test_URL='mysql+pymysql://user:pass@host:port/dbname1' icp-managementServers
 # Check the logs
 docker logs -f icp-managementServers
 # Cleaup the container
 docker stop icp-managementServers && docker rm icp-managementServers
 ```
## To Run UnitTests & Integration tests
```bash
python -m unittest -v src/tests/unit_mocktests.py
python -m unittest -v src/tests/integration_test.py
```
 ## To Run the SWAGGER UI
 ```bash
 http://{ipaddress}:{PORT}/apidocs/
```
## To Check code coverage
```
pylint  /path/to/project --reports=y  --ignored-classes=SQLAlchemy,scoped_session --disable=invalid-name,locally-disabled,arguments-differ,no-value-for-parameter,useless-object-inheritance,superfluous-parens,no-else-return,too-many-instance-attributes,no-self-argument,len-as-condition,singleton-comparison,attribute-defined-outside-init,cyclic-import,unused-variable,attribute-defined-outside-init,wrong-import-order,wrong-import-position
```
## Author
Mattareddy Syamala