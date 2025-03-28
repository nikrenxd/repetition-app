## Running the Project

### Running via docker-compose
To run the project, you will need to have Docker and Docker Compose installed on your device.
The project is launched using the Makefile commands
#### For local environment:
```shell
  make up
```

### After launchig project
After you launch project, create database tables with 2 commands
```shell
  docker compose exec web-app python manage.py makemigrations
  
  docker compose exec web-app python manage.py migrate
```

### Tests
To run tests simply use Makefile command while app is running via Docker:
```shell
  make test
```
